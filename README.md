# the_final_task_for_stepik

Для запуска тестов необходимо:
1. Скопировать репозиторий через SHH (git clone)
2. Загрузите chromedriver для вашей операционной системы и соответствующую версию
и поместите ее в переменную PATH.
3. Создайте виртуальную среду и войдите в нее(
win:python -m venv venv, venv/Scripts/activate, linux: python -m ven ven, source venv/bin/activate)
4. Загрузите все модули в виртуальную среду (pip3 install -r requirements.txt )
5. Для генирации отчетов в Allure понадобится дополительно установка:
Allure документация по установке - https://docs.qameta.io/allure-report/#_installing_a_commandline,
https://github.com/ScoopInstaller/Scoop
OpenJDK документация по установке - https://learn.microsoft.com/ru-ru/java/openjdk/download,
https://docs.oracle.com/cd/E19182-01/820-7851/inst_cli_jdk_javahome_t/
6. Тесты выполняются из корневой дириктории командой: pytest -v -s --alluredir=/reports
7. Просмотреть отчет: allure allure serve /reports
