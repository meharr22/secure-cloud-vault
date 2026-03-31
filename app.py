from flask import Flask, request, redirect, url_for, session, send_file
import boto3
from io import BytesIO

app = Flask(__name__)
app.secret_key = "securecloudsecret"

# ================= AWS CONFIG =================
BUCKET = "meharproject"   

s3 = boto3.client("s3", region_name="us-east-1")

# ================= LOGIN =================
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username == "admin" and password == "admin123":
            session["user"] = username
            return redirect("/upload")
        else:
            return "Invalid credentials!"

    return '''
        <h2>Login - SecureCloud Vault</h2>
        <form method="post">
            Username: <input name="username"><br><br>
            Password: <input type="password" name="password"><br><br>
            <button type="submit">Login</button>
        </form>
    '''

# ================= UPLOAD =================
@app.route("/upload", methods=["GET", "POST"])
def upload():
    if "user" not in session:
        return redirect("/")

    if request.method == "POST":
        file = request.files["file"]
        s3.upload_fileobj(file, BUCKET, file.filename)
        return "<h3>File uploaded successfully!</h3><a href='/files'>View Files</a>"

    return '''
        <h2>Upload File</h2>
        <form method="post" enctype="multipart/form-data">
            <input type="file" name="file">
            <button type="submit">Upload</button>
        </form>
        <br><a href="/files">View Files</a>
        <br><br><a href="/logout">Logout</a>
    '''

# ================= FILE LIST =================
@app.route("/files")
def list_files():
    if "user" not in session:
        return redirect("/")

    response = s3.list_objects_v2(Bucket=BUCKET)
    files = response.get("Contents", [])

    output = "<h2>Uploaded Files</h2>"

    for file in files:
        filename = file["Key"]
        output += f"""
        {filename}
        <a href='/download/{filename}'>Download</a>
        <a href='/versions/{filename}'>Versions</a>
        <br><br>
        """

    output += "<br><a href='/upload'>Upload More</a>"
    output += "<br><br><a href='/logout'>Logout</a>"
    return output

# ================= DOWNLOAD =================
@app.route("/download/<filename>")
def download_file(filename):
    if "user" not in session:
        return redirect("/")

    file_obj = s3.get_object(Bucket=BUCKET, Key=filename)

    return send_file(
        BytesIO(file_obj["Body"].read()),
        download_name=filename,
        as_attachment=True
    )

# ================= VERSIONING =================
@app.route("/versions/<filename>")
def file_versions(filename):
    if "user" not in session:
        return redirect("/")

    versions = s3.list_object_versions(Bucket=BUCKET, Prefix=filename)

    output = f"<h2>Versions of {filename}</h2>"

    for version in versions.get("Versions", []):
        version_id = version["VersionId"]
        output += f"""
        Version ID: {version_id}
        <a href='/download_version/{filename}/{version_id}'>Download</a>
        <br><br>
        """

    output += "<br><a href='/files'>Back</a>"
    return output

@app.route("/download_version/<filename>/<version_id>")
def download_version(filename, version_id):
    if "user" not in session:
        return redirect("/")

    file_obj = s3.get_object(
        Bucket=BUCKET,
        Key=filename,
        VersionId=version_id
    )

    return send_file(
        BytesIO(file_obj["Body"].read()),
        download_name=filename,
        as_attachment=True
    )

# ================= LOGOUT =================
@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect("/")

# ================= RUN =================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)