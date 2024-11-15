# Backend-Carpooling

# Version: 1.0

## Requerimientos
   - Archivo serviceAccountKey.json
   ```json
    {
        "type": "service_account",
        "project_id": "carpooling-a1892",
        "private_key_id": "7a8a956asd345dba2f5af72f1acacf90k64f6ddb",
        "private_key": "-----BEGIN PRIVATE KEY----- -----END PRIVATE KEY-----",
        "client_email": "firebase-adminsdk-36ppm@carpooling-d7882.iam.gserviceaccount.com",
        "client_id": "114906384510979294766",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/fir....iam.gserviceaccount.com",
        "universe_domain": "googleapis.com"
    }
   ```
   - Archivo .env
   ```json
    DATABASE_URI=""
    AUTH0_CLIENT_ID=""
    AUTH0_CLIENT_SECRET=""
    AUTH0_DOMAIN=""
    APP_SECRET_KEY=""
    GOOGLE_CLIENT_ID=""
    EXPO_PUBLIC_ACCESS_TOKEN=""
   ```
## Iniciar el proyecto
   ```bash
   pip install -r .\req.txt
   ```
   ```bash
   py .\app.py
   ```


Backend corriendo en remoto: [dscarpooling-back.alwaysdata.net](dscarpooling-back.alwaysdata.net)
