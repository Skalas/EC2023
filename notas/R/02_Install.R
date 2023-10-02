---
title: "Instalación R"
output: 
  html_document:
    toc: yes
    toc_depth: 2
    toc_float: true
    theme: spacelab
---

```{r setup, include=FALSE}
knitr::opts_chunk$set(echo = TRUE)
```

# R
Lo primero que debemos hacer es instalar R. 

## Windows 
En windows la última versión está en [este link.](https://cran.itam.mx/bin/windows/base/release.htm)

## Mac
Necesitamos instalar [Xquartz](https://www.xquartz.org/), antes estaba dentro del sistema operativo pero ya no, por lo que tenemos que instalarlo manualmente, usen la versión estable, no acepten versiones de desarrollo. 

Necesitamos también XCode 12.4.

Con los dos prerrequisitos podemos instalar [R](https://cran.r-project.org/bin/macosx/R-4.0.5.pkg).

## Ubuntu/Linux

```{bash, eval=FALSE}
sudo apt update && sudo apt install r-base
```

# Rstudio

Ir a [esta página](https://www.rstudio.com/products/rstudio/download/) para descargar la última versión de Rstudio. Aquí están las versiones para la mayoría de las plataformas(al menos todas las que tenemos los presentes :) ). 

# Git 

Para instalar `git` en sus computadoras ir al [siguiente link](http://git-scm.com/downloads) y seguir las instrucciones para el sistema operativo correcto. 

# Editores de texto Opcionales

Se recomienda que además de Rstudio, también tengan un editor de texto de confianza. 
  * Mi preferencia personal es [Emacs](https://www.gnu.org/software/emacs/?), con [Ess](https://ess.r-project.org/), sin embargo la curva de aprendizaje puede ser dura.
  * Otro buen editor de texto que vino a revolucionar los editores de texto es [Visual Studio Code](https://code.visualstudio.com/). 
