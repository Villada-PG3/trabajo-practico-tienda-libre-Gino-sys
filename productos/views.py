from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def inicio(request):
    return HttpResponse("""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Tienda Django</title>
        <style>
            *{
                margin:0;
                padding:0;
                box-sizing:border-box;
                font-family:Arial, Helvetica, sans-serif;
            }

            body{
                background:linear-gradient(135deg,#4facfe,#00f2fe);
                height:100vh;
                display:flex;
                justify-content:center;
                align-items:center;
            }

            .contenedor{
                background:white;
                padding:50px;
                border-radius:20px;
                box-shadow:0 10px 25px rgba(0,0,0,.2);
                text-align:center;
                max-width:700px;
            }

            h1{
                color:#2c3e50;
                font-size:42px;
                margin-bottom:20px;
            }

            p{
                color:#555;
                font-size:20px;
                margin-bottom:30px;
            }

            .admin{
                background:#0d6efd;
                color:white;
                display:inline-block;
                padding:15px 25px;
                border-radius:10px;
                font-size:22px;
                font-weight:bold;
            }

            code{
                background:#f1f1f1;
                color:#d63384;
                padding:3px 8px;
                border-radius:5px;
                font-size:20px;
            }

            footer{
                margin-top:35px;
                color:#888;
                font-size:15px;
            }
        </style>
    </head>
    <body>

        <div class="contenedor">
            <h1>🚀 Bienvenido a la Tienda Django</h1>

            <p>
                El servidor se encuentra funcionando correctamente.
            </p>

            <div class="admin">
                Escribí <code>/admin</code> en la barra de direcciones
                para acceder a la <strong>gestión de la tienda</strong>.
            </div>

            <footer>
                Proyecto desarrollado con Django 🐍
            </footer>
        </div>

    </body>
    </html>
    """)