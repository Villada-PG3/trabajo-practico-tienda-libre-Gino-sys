1. Obtener todos los productos — all()
Producto.objects.all()

Obtiene todos los productos registrados en la base de datos.

El método all() devuelve un QuerySet con todos los objetos del modelo Producto.

2. Obtener productos con precio mayor a 5 — filter() y __gt
Producto.objects.filter(precio__gt=5)

Obtiene los productos cuyo precio sea mayor a 5.

El lookup __gt significa mayor que (greater than).

3. Obtener productos con precio menor a 1 — filter() y __lt
Producto.objects.filter(precio__lt=1)

Obtiene los productos cuyo precio sea menor a 1.

El lookup __lt significa menor que (less than).

4. Buscar productos por nombre — __icontains
Producto.objects.filter(nombre__icontains="leche")

Busca productos cuyo nombre contenga la palabra "leche" sin distinguir entre mayúsculas y minúsculas.

El lookup __icontains permite realizar búsquedas de texto.

5. Obtener productos con stock mayor a 100
Producto.objects.filter(stock__gt=100)

Obtiene los productos que tengan un stock mayor a 100 unidades.

6. Excluir productos con stock menor a 50 — exclude()
Producto.objects.exclude(stock__lt=50)

Obtiene todos los productos excepto aquellos que tengan un stock menor a 50 unidades.

En este caso se combinan el método exclude() y el lookup __lt.

7. Ordenar productos por precio de mayor a menor — order_by()
Producto.objects.order_by("-precio")

Ordena todos los productos desde el precio más alto hasta el más bajo.

El signo - antes del nombre del campo indica un orden descendente.

8. Buscar productos con determinados precios — __in
Producto.objects.filter(precio__in=[1.10, 1.50, 2.10])

Obtiene los productos cuyo precio sea alguno de los valores indicados.

El lookup __in permite buscar objetos cuyo valor se encuentre dentro de una lista.

9. Obtener un producto específico — get()
Producto.objects.get(pk=24)

Obtiene un único producto utilizando su clave primaria.

El método get() busca exactamente un objeto y devuelve directamente ese objeto.

A diferencia de filter(), que devuelve un QuerySet, get() devuelve un único objeto.

Esta consulta supone que existe un producto con pk=1.

10. Navegar relaciones entre Producto y Categoría

-Desde una categoría hacia sus productos
categoria = Categoria.objects.get(nombre="Bebida")

categoria.productos.all()

Primero se obtiene la categoría "Bebida".

Luego, categoria.productos.all() obtiene todos los productos que pertenecen a esa categoría.

-Desde un producto hacia su categoría
producto = Producto.objects.exclude(categoria__isnull=True).first()

producto.categoria.nombre

Obtiene un producto que tenga una categoría asignada y permite acceder al nombre de su categoría.

11. CREAR UN PRODUCTO DESDE EL SHELL
categoria = Categoria.objects.get(nombre="Bebida")

Producto.objects.create(
    categoria=categoria,
    nombre="Leche",
    descripcion="Leche entera",
    precio=2.50,
    stock=100,
    marca="La Serenísima"
)