# Тизер решения
Решение кейса представляет собой десктопное приложение, позволяющее идентифицировать различных особей гренландского кита.

В основе его работы лежит алгоритм распознавания отличительных признаков особей кита — шрамов и меток на спине, хвосте и морде. Модель обучена распознавать и отличать данные признаки — таким образом разработанное нашей командой приложение идентифицирует китов.

# Уникальность
Если не удаётся идентифицировать кита на фотографии как одного из уже известных, приложение определяет его как новую особь. 

# Стек технологий
* Python
* TensorFlow, PyTorch
* PyQt5

# Результаты
![image](https://user-images.githubusercontent.com/112272101/201511363-82c4d662-8daf-4f82-afcb-e8ea73dccb14.png)
(графики тренировки модели)

# Run the program 
Необходимо установить pyinstaller, после чего запустить команду

pyinstaller --noconfirm --onedir --windowed --icon "~ /AI_gamers/ico3.ico" 
--add-data "~ /AI_gamers/ui.py;." 
--add-data "~ /AI_gamers/ico3.ico;." 
--add-data "~ /AI_gamers/hXception.h5;." 
--hidden-import "h5py" 
--hidden-import "h5py.defs" 
--hidden-import "h5py.utils" 
--hidden-import "h5py.h5ac" 
--hidden-import "h5py._proxy"  "~/AI_gamers/Ai Games Bowhead whale.py"

# AI геймеры
**ML engineers**
* **Эдуард Северьянов** 
* [**Христина Першина**](https://github.com/NorthernPeach)
* **Владимир Губин** 
* **Кристина Иванова** 

**UX/UI designer**
* [**Дмитрий Ермилов**](https://github.com/aiker95)

*Проект выполнен на окружном хакатоне «Цифровой прорыв: Сезон Искусственный интеллект» в Северо-Кавказском федеральном округе (г. Ставрополь) с 11 по 13 ноября 2022 года, вошёл в топ-__ решений кейса «ИИ в поисках гренландского кита» от Минприроды России*
