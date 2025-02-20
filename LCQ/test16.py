import base64

encoded_string = "dBGLLP4BZoo42uSXR25rqoQoKw+v0VuGw/r49fg0eE3FwV4WoYdN3bauIyC3wmyYB3MJDs43pijpmL8D/bTmIF31oiJiYD61QE80fMw+zP44SPUb4KYcATNPCInjgkNkVgQ="
decoded_bytes = base64.b64decode(encoded_string)
decoded_string = decoded_bytes.decode('utf-8', errors='ignore')

print(decoded_string)
