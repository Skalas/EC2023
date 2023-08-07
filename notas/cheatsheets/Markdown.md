# Markdown

*Basado en [este cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#links) y [este otro](https://www.stack.nl/~dimitri/doxygen/manual/markdown.html)*

Estamos acostumbrados a editores del tipo *what you see is what you get*. Markdown permite escribir contenidos en **texto plano**.

Tiene un alfabeto y símbolos que, una vez procesados, se ven de cierta forma. Lo que lo hace grandioso es que, a diferencia de un editor como word en el que la versión de cada computadora cambia la manera en la que se ven los documentos, con markdown esto no sucede.

Este lenguaje se está volviendo cada vez más común y, en particular, páginas como GitHub y reddit lo utilizan para sus comentario.

La curva de aprendizaje es mínima. En lo que se va memorizando el alfabeto de markdown, lo más útil es tener una lista de fácil acceso con los caracteres más comúnes y lo que hacen.

## Encabezados

```
# Nivel 1
## Nivel 2
### Nivel 3
#### Nivel 4

... y asi
```

# Nivel 1
## Nivel 2
### Nivel 3
#### Nivel 4

## Lineas horizontales

Con tres o mas de los siguientes

```
---

Guiones

***
Asteriscos

___

Guiones bajos
```

---

Guiones

***
Asteriscos

___

Guiones bajos

## Énfasis

```
*italica* o _italica_
**negritas** o __negritas__
**_combinado_**
**Uno en negritas _el otro combinado_**
~~tachar~~
```

- *italica* o _italica_
- **negritas** o __negritas__
- **_combinado_**
- **Uno en negritas _el otro combinado_**
- ~~tachar~~

## Bloques

```
> Ejemplo: Un bloque de varias
> lineas.
```

> Ejemplo: Un bloque de varias
> lineas.

## Listas

```
1. Primero
2. Segundo
    - Primer elemento del segundo
    - Segundo elemento del segundo
7. No tengo que cambiar el nombre, se pondra el correcto
    i. Una sublista con incisos
    ii. Mas incisos
4. Mas cosas
    a. Otra cosa
    b. Una mas
5. Otra manera de hacer listas no ordenadas
    * Usando asteriscos
    - O usando menos
    - O usando el signo de mas
```

1. Primero
2. Segundo
    - Primer elemento del segundo
    - Segundo elemento del segundo
7. No tengo que cambiar el nombre, se pondra el correcto
   1. Una sublista con incisos
   2. Mas incisos
4. Mas cosas
   1. **Otra cosa**
   5. Una mas
5. Otra manera de hacer listas no ordenadas
    * Usando asteriscos
    - O usando menos
    - O usando el signo de mas

## Links

```
[Esto es lo que se ve](https://www.google.com)

[Esto es lo que se ve y el mensaje "Google" aparece en el hover](https://www.google.com "Google")

[Puedo hacer referencia a un archivo local](readme.md)

[Puedes poner referencias con numeros][1]

Luego quieres hacer referencias a otra parte del documento [por lo tanto, puedes ligar texto]

Detecata urls completos http://www.google.com

Y luego pones a donde te lleva la referencia

[1]: https://en.wikipedia.org/wiki/42_%28number%29#The_Hitchhiker.27s_Guide_to_the_Galaxy

[por lo tanto, puedes ligar texto]: http://www.reddit.com

Nota que los espacios entre lineas son importantes.

```

[Esto es lo que se ve](https://www.google.com)

[Esto es lo que se ve y el mensaje "Google" aparece en el hover](https://www.google.com "Google")

[Puedo hacer referencia a un archivo local](Readme.md)

[Puedes poner referencias con numeros][1]

Luego quieres hacer referencias a otra parte del documento [por lo tanto, puedes ligar texto]

Detecata urls completos http://www.google.com

Y luego pones a donde te lleva la referencia

[1]: https://en.wikipedia.org/wiki/42_%28number%29#The_Hitchhiker.27s_Guide_to_the_Galaxy

[por lo tanto, puedes ligar texto]: http://www.reddit.com

Nota que los espacios entre lineas son importantes.

## Imágenes

```
Puedes ponerlo en una misma linea:
![alt text](https://upload.wikimedia.org/wikipedia/commons/5/58/Doctor_Who_logo_1963-1967.jpg "Es lo mejor")

Reference-style:
![alt text][logo]

[logo]: https://upload.wikimedia.org/wikipedia/commons/5/58/Doctor_Who_logo_1963-1967.jpg "Sin duda alguna"
```

Puedes ponerlo en una misma linea:
![alt text](https://upload.wikimedia.org/wikipedia/commons/5/58/Doctor_Who_logo_1963-1967.jpg "Es lo mejor")

Reference-style:
![alt text][logo]

[logo]: https://upload.wikimedia.org/wikipedia/commons/5/58/Doctor_Who_logo_1963-1967.jpg "Sin duda alguna"


## Tablas

```
Una tabla simple

Encabezado 1  | Encabezado dos
------------- | --------------
Contenido     | Contenido
Contenido     | Contenido
```

Encabezado 1  | Encabezado dos
------------- | --------------
Contenido     | Contenido
Contenido     | Contenido

```
Una tabla alineada. La alineacion la puedes hacer por columnas

| Derecha | Centro | Iquierda |
| ----: | :----: | :---- |
| 10    | 10     | 10    |
| 1000  | 1000   | 1000  |
```

| Derecha | Centro | Iquierda |
| ----: | :----: | :---- |
| 10    | 10     | 10    |
| 1000  | 1000   | 1000  |

## HTML

Si sabes html, puedes utilizarlo directo.

```
<dl>
  <dt>Lista de definiciones</dt>
  <dd> Una def.</dd>

  <dt>Markdown en HTML</dt>
  <dd>No *siempre* funciona muy **bien**. Usa puro HTML <em>para que funcione siempre</em>.</dd>
</dl>

Puedes controlar mejor las imagenes

<img src="img/imagen.svg" align="middle" height="50" width="75" margin="0 auto" />
```

<dl>
  <dt>Lista de definiciones</dt>
  <dd> Una def.</dd>

  <dt>Markdown en HTML</dt>
  <dd>No *siempre* funciona muy **bien**. Usa puro HTML <em>para que funcione siempre</em>.</dd>
</dl>

Puedes controlar mejor las imagenes

<img src="img/imagen.svg" align="middle" height="50" width="75" margin="0 auto" />

## Código

```
En una linea puedo poner `codigo`
```

En una linea puedo poner `codigo`.

Para poner bloques de codico se utilizan tres acentos invertidos y se especifica el lenguaje.

```python
import requests
print "Hola mundo!"
```

```sql
select * from tabla;
```

```r
library(reshape2)
```

```
Sin lenguaje, no lo resalta
```

## Parrafos

```
Si
escribo asi
me lo junta todo.

Debo separar para iniciar otro parrafo.
```

Si
escribo asi
me lo junta todo.

Debo separar para iniciar otro parrafo.
