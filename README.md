<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a id="readme-top"></a>

<!-- PROJECT LOGO -->
<br />
<div align="center">
<h3 align="center">Школьный сервис</h3>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Подробнее</summary>
  <ol>
    <li>
      <a href="#about-the-project">О проекте</a>
      <ul>
        <li><a href="#built-with">Стэк</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Начнём!</a>
      <ul>
        <li><a href="#prerequisites">Предустановки</a></li>
        <li><a href="#installation">Установка</a></li>
      </ul>
    </li>
    <li><a href="#usage">Использование</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## О проекте

Это школьный сервис

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Стэк

* docker compose
* postresql

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Как начать

Для запуска проекта вам понадобяться несколько приложений и предварительная настройка конфигов

### Предустановки
* Mac OS
  ```sh
  brew install docker
  ```
* Linux
  * Ubuntu
  ```sh
    sudo apt install docker docker-compose
  ```
  * Arch
  ```sh
    sudo yay -S docker docker-compose
  ```
* Windows
  Установите docker к себе на компьютер

Далее идёт настройка конфигов. Задайте все нужные параметры в example.env и переименуйте его в .env

### Installation

1. Склонируйте этот репозиторй себе и откройте его в консоли
2. Выполните комманду
  ```sh
    docker compose up -d --build
  ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Использование

#### Этот репозиторий нужен для добавления новых модулей в сервис.
#### Чтобы добавить новый модуль нужно создать новый git submodule в папке с этим репозиторием у себя на устройстве. Далее потребуется написать конфигурацию контейнера либо только в docker-compose.yaml, либо написать конфигурацию в папке с своим проектом, назвав её Dockerfile и интегрировав его в docker-compose.yaml(В случае с модулем авторизации так и сделано). 
#### Если в вашем модуле есть порты, то нужно резервировать исключительно те, которые свободны внутри docker-compose, либо создавать сеть внутри docker-compose.yaml, которая будет относиться только к вашему модулю.
#### После того как вы удостоверились в том, что ваш код работает, вам требуеться создать pull request в ветку dev и в ближайшем будующем вам ответит автор, либо ваш код просто сольют в ветку и он будет работать.

### В будующем будет добавлен nginx внутрь docker-compose для упрощённого взаимодействия с модулями из вне.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTACT -->
## Контакты

Всеволод - [Telegram](https://t.me/sevstarQ)

<p align="right">(<a href="#readme-top">back to top</a>)</p>
