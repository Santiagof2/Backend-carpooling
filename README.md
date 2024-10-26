# Backend-Carpooling
# Version: 1.0

## Iniciar el proyecto
   ```bash
   pip install -r .\req.txt
   ```
   ```bash
   py .\app.py
   ```

Coleccion de Postman en docs/
/users:
{
    / GET #Retorna todos los usuarios
    / POST #Crea un usuario
    /:id PUT #Actualiza un usuario
    /:id DELETE #Elimina un usuario
    /:id GET #Obtiene detalles de un usuario
}
/trip:
{
    / GET #Retorna todos los viajes
    / POST #Crea un viaje
    /:id GET #obtiene detalles de un viaje
}
/trip_join:
{
    / POST #Une un pasajero con un viaje
}
/role:
{
    /select_role POST #modifica el rol del usuario
}

Backend corriendo en remoto: [dscarpooling-back.alwaysdata.net](dscarpooling-back.alwaysdata.net)
