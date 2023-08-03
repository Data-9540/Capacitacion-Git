# Bienvenido al mundo de GIT!

Git es un proyecto de código abierto maduro y con un mantenimiento activo que desarrolló originalmente Linus Torvalds, el famoso creador del kernel del sistema operativo Linux, en 2005


# Comandos

StackEdit stores your files in your browser, which means all your files are automatically saved locally and are accessible **offline!**

## Create files and folders

The file explorer is accessible using the button in left corner of the navigation bar. You can create a new file by clicking the **New file** button in the file explorer. You can also create folders by clicking the **New folder** button.

## Ayuda de Git para uso diario, menos de 20 comandos para usar git diariamente. 
git help everyday

## Muestra la guía de Ayuda de Git 
git help -g

## Sobreescribir pull 
git fetch --all && git reset --hard origin/master

## Lista de todos los archivos hasta un commit 
git ls-tree --name-only -r

## Actualizar la referencia al primer commit 
git update-ref -d HEAD

## Lista de todos los archivos en conflicto 
git diff --name-only --diff-filter=U

## Lista de todos los archivos cambiados en el commit 
git diff-tree --no-commit-id --name-only -r

## Ver los cambios que haz hecho desde el último commit 
git diff

## Compara tus cambios preparados con tu último commit 
git diff --cached

## Muestra la diferencia entre los cambios registrados y no registrados 
git diff HEAD

## Lista todos los branches que ya han hecho merged con tu master 
git branch --merged master

## Cambia rápidamente al branch anterior 
git checkout -

## Quita los branch que ya han sido fusionados con la master 
git branch --merged master | grep -v '^*' | xargs -n 1 git branch -d

## Lista todas las ramas y sus últimos commit con el branch 
git branch -vv

## Realiza un seguimiento del branch 
git branch -u origin/mybranch

## Elimina un branch local 
git branch -d <local_branchname>

## Elimina un branch remoto 
git push origin --delete <remote_branchname>

## Deshacer cambios locales con el último contenido en la cabeza 
git checkout -- <file_name>

## Revierte un commit creando un nuevo commit 
git revert

## Descarta un commit, se recomienda sólo en branch privados 
git reset

## Cambia el mensaje del commit anterior 
git commit -v --amend

## Modifica el Autor 
git commit --amend --author='Author Name [email@address.com](mailto:email@address.com)'

## Restablece el autor, después de que el autor a sido cambiado en la configuración global 
git commit --amend --reset-author --no-edit

## Cambia la URL remota
git remote set-url origin

## Obtiene una lista de todas las referencias remotas 
git remote Alternativa: git remote show

## Obtiene una lista de todos los branches locales y remotos 
git branch -a

## Obtiene una lista de los branches remotos 
git branch -r

## Añade las parte que cambiaron de un archivo, en lugar de todo el archivo 
git add -p

## Busca los bash completados 
curl [http://git.io/vfhol](http://git.io/vfhol) > ~/.git-completion.bash && echo '[ -f ~/.git-completion.bash ] && . ~/.git-completion.bash' >> ~/.bashrc

## Muestra los cambios de las últimas 2 semanas 
git log --no-merges --raw --since='2 weeks ago' Alternativas: git whatchanged --since='2 weeks ago'

## Visualiza todos los commit de los fork del master 
git log --no-merges --stat --reverse master..

## Selección de commits a través de los branches usando cherry-pick 
git checkout && git cherry-pick

## Encuentra los branches que contienen commit hash 
git branch -a --contains Alternativa: git branch --contains

## Alias de Git 
git config --global alias. git config --global alias.st status

## Guarda rápidamente y de manera provisional (stasheado) los trabajos realizados git stash Alternativa: git stash save

## Stasheado de todos los archivos, inclusos los que no están preparados. git stash save -u Alternativa: git stash save --include-untracked

## Montrar lista de todos los archivos stasheado git stash list

## Usar cualquier cambio stasheado sin borrarlo de la lista de stasheados git stash apply <stash@{n}>

## Reaplicar los cambios stasheados y sacarlo de la lista de stasheados 
git stash pop Alternatives: git stash apply stash@{0} && git stash drop stash@{0}

## Borrar todos los stashes almacenados 
git stash clear Alternatives: git stash drop <stash@{n}>

## Tomar un archivo específico que haya sido stasheado 
git checkout <stash@{n}> -- <file_path> Alternativa: git checkout stash@{0} -- <file_path>

## Mostrar todos los archivos preparados 
git ls-files -t

## Mostrar todos los archivos que no han sido preparados 
git ls-files --others

## Mostrar todos los archivos ignorados 
git ls-files --others -i --exclude-standard

## Crear un nuevo árbol de trabajo de un repositorio (git 2.5) 
git worktree add -b

## Crear un nuevo árbol de trabajo desde un HEAD 
git worktree add --detach HEAD

## Eliminar un archivo del repositorio git sin eliminarlo del respositorio local 
git rm --cached <file_path> Alternativa: git rm --cached -r <directory_path>

## Antes de eliminar archivos sin preparar, hacer un recorrido de prueba para obtener la lista de estos archivos. 
git clean -n

## Forzar la eliminación de archivos sin preparar 
git clean -f

## Forzar la eliminación de directorios sin preparar 
git clean -f -d Alternativa: git clean -df

## Actualizar todos los submódulos 
git submodule foreach git pull

## Muestra todos los cambios del branch actual que no han hecho merged con el master 
git cherry -v master Alternativa: git cherry -v master

## Renombrar un branch 
git branch -m Alternativa: git branch -m []

## Actualizar ‘feature’ y hacer merged ‘master’ 
git checkout feature && git rebase @{-1} && git checkout @{-2} && git merge @{-1}

## Archivar el branch master 
git archive master --format=zip --output=master.zip

#Modificar el commit anterior sin modificar el mensaje del informe git add --all && git commit --amend --no-edit

#Eliminar las ramas remotas que ya no existan en origin git fetch -p Alternativa: git remote prune origin

#Recuperar el commit hash de la revisión inicial git rev-list --reverse HEAD | head -1

#Visualiza el árbol de versiones git log --pretty=oneline --graph --decorate --all Alternativa: gitk --all

#Añadir un proyecto a un repositorio usando subárbol git subtree add --prefix=<directory_name>/<project_name> --squash [git@github.com](mailto:git@github.com):/<project_name>.git master

#Obtiene los últimos cambios de tu repositorio para un proyecto vinculado utilizando subárbol git subtree pull --prefix=<directory_name>/<project_name> --squash [git@github.com](mailto:git@github.com):/<project_name>.git master

#Exporta un branch y su historial a un archivo git bundle create

#Importa desde un bundle git clone repo.bundle -b

#Obtiene el nombre del branch actual git rev-parse --abbrev-ref HEAD

#Ignora un archivo que ya le han hecho commit(e.g. Changelog). git update-index --assume-unchanged Changelog; git commit -a; git update-index --no-assume-unchanged Changelog

#Stashea los cambios antes de reorganizar git rebase --autostash

#Busca por id en el branch local git fetch origin pull//head: Alternatives: git pull origin pull//head:

#Muestra los tag más recientes de la rama actual git describe --tags --abbrev=0

#Busca diferencias. git diff --word-diff

#No tiene en cuenta los cambios en el archivo de seguimiento git update-index --assume-unchanged <file_name>

#Deshacer git update-index --no-assume-unchanged <file_name>

#Limpiar los archivos de .gitignore. git clean -X -f

#Restaurar archivo eliminado. git checkout <deleting_commit>^ -- <file_path>

#Restaurar archivos con un commit-hash específico git checkout -- <file_path>

#Siempre reorganizar en lugar de hacer merge git config --global branch.autosetuprebase always

#Listar todos los alias y las configuraciones git config --list

#Hacer caso git sensible git config --global core.ignorecase false

#Tipos de autocorreción. git config --global help.autocorrect 1

#Comprueba si el cambio es parte de un release. git name-rev --name-only

#Limpiar Dry run. git clean -fd --dry-run

#Marca el commit como una solución al commit anterior git commit --fixup

#Correción de squash git rebase -i --autosquash

#Salta el area de ensayo durante el commit. git commit -am

#Listar los archivos ignorados git check-ignore *

#Status de los archivos ignorados git status --ignored

#Commits en el Branch1 que no están en el Branch2 git log Branch1 ^Branch2

#grabar y reutilizar anteriores resoluciones de conflictos git config --global rerere.enabled 1

#Abra todos los archivos en conflicto en un Editor. git diff --name-only | uniq | xargs $EDITOR

#Cuenta el número de objetos sin preparar y su consumo en el disco. git count-objects --human-readable

#Mantenimiento de los objetos inaccesibles git gc --prune=now --aggressive

#Visualiza al instante su repositorio en gitweb. git instaweb [--local] [--httpd=] [--port=] [--browser=]

#Visualiza las firmas GPG en el log de confirmación git log --show-signature

#Elimina entradas de la configuración global. git config --global --unset

#Obtenga una nueva rama sin historial git checkout --orphan <branch_name>

#Visualiza la diferencia entre el archivo de producción y la última versión del mismo. git diff --staged

#Extraer un archivo de otro branch. git show <branch_name>:<file_name>

#Lista sólo la raiz y confirma el merge git log --first-parent

#Hace merge entre dos commit git rebase --interactive HEAD~2

#Lista todos los branch git checkout master && git branch --no-merged

#Encuentra utilizando búsqueda binaria git bisect start  
git bisect bad  
git bisect good v2.6.13-rc2  
git bisect bad  
git bisect good  
git bisect reset

#Lista los commits y cambios de un archivo en específico git log --follow -p -- <file_path>

#Clona un sólo branch git clone -b --single-branch [https://github.com/user/repo.git](https://github.com/user/repo.git)

#Crea y cambia a un nuevo branch git checkout -b

#Ignora los archivos que tengan cambios en los commits git config core.fileMode false
```
