## Video Gallery API

Simple API service to fetch the latest videos from youtube for a
search key(word), store in DB and expose it via APIs.


#### Setup Instructions

1. Add your Google Application API Key for Youtube API.
    - `YOUTUBE_API_KEY` in `.env.dev`

2. Add your search word against which videos will be fetched
    - `YOUTUBE_SEARCH_KEYWORD` in `.env.dev`
    - If not given, `'football'` will be used.

3. use docker-compose to run the service
    -
    ```
    git clone git@github.com:imkaka/video-gallery-api.git
    cd video-gallery-api

    docker-compose up -d --build
    ```
    - It will run 4 services.
        - Web: Our Django DRF API Service
        - Celery: To run background task(Fetching Videos)
        - Celery Beat - To Schedule Tasks in given interval
        - DB - Our Postgres Database Instance
        - Redis - Used as a Broker and backend for celery.


4. How to Test?
    1. Dashboard - `http://localhost:8000/admin/gallery/video/`
        - To access Dashboard, we need to create a superuser
        -
        ```
        docker-compose exec web python manage.py createsuperuser
        ```

    2. List API (Videos in descending order of published datetime)
        -
        ```
        curl --location --request GET 'localhost:8000/api/v1/video/?page_size=5'
        ```
        - `page_size` is optional, if not given will pick the default value.

    3. Search API
        -
        ```
        curl --location --request GET 'localhost:8000/api/v1/video/search/?q=ronaldo&page_size=5'
        ```
        - This API is also paginated, `q` will be searched in `title` and `description` of the video.

5. Note - We can stop the celery beat service after sometime otherwise it will keep
fetching videos and store in DB.
    - You can change the interval in `CELERY_BEAT_SCHEDULE` config of `settings.py`

Examples:

1. List API

```
curl --location --request GET 'localhost:8000/api/v1/video/?page_size=3'

{
    "next": "http://localhost:8000/api/v1/video/?cursor=cD0yMDIxLTA4LTI0KzE5JTNBMDAlM0EwOSUyQjAwJTNBMDA%3D&page_size=3",
    "previous": null,
    "results": [
        {
            "id": 51,
            "video_source": "youtube",
            "title": "LIVE: Big Ten, ACC, Pac 12 Alliance is Official | 365 Sports | 8.24.21 | Big 12, SEC",
            "description": "Get your college football gear: https://fanatics.93n6tx.net/DVb0X2 Join David Smoak, Paul Catalina and Craig Smoak on 365 Sports Radio weekdays from 3-6 ...",
            "published_at": "2021-08-24T19:58:31Z",
            "created_at": "2021-08-24T20:38:00.743422Z",
            "thumbnails": {
                "high": {
                    "url": "https://i.ytimg.com/vi/tOjFB2cZDJ4/hqdefault_live.jpg",
                    "width": 480,
                    "height": 360
                },
                "medium": {
                    "url": "https://i.ytimg.com/vi/tOjFB2cZDJ4/mqdefault_live.jpg",
                    "width": 320,
                    "height": 180
                },
                "default": {
                    "url": "https://i.ytimg.com/vi/tOjFB2cZDJ4/default_live.jpg",
                    "width": 120,
                    "height": 90
                }
            }
        },
        {
            "id": 551,
            "video_source": "youtube",
            "title": "Half-PPR Mock Draft 4.0 (2021) | Fantasy Football Pick-by-Pick Strategy + Player Advice",
            "description": "Joey P., Dan Harris, and Kyle Yates are back for a Half-PPR mock draft! Listen all the way through to find out who had the best draft. Weigh-in below with your ...",
            "published_at": "2021-08-24T19:55:30Z",
            "created_at": "2021-08-24T21:38:12.102655Z",
            "thumbnails": {
                "high": {
                    "url": "https://i.ytimg.com/vi/_qvY-KqoM9c/hqdefault.jpg",
                    "width": 480,
                    "height": 360
                },
                "medium": {
                    "url": "https://i.ytimg.com/vi/_qvY-KqoM9c/mqdefault.jpg",
                    "width": 320,
                    "height": 180
                },
                "default": {
                    "url": "https://i.ytimg.com/vi/_qvY-KqoM9c/default.jpg",
                    "width": 120,
                    "height": 90
                }
            }
        },
        {
            "id": 552,
            "video_source": "youtube",
            "title": "Rookie Power Rankings After Preseason Week 2 | Good Morning Football",
            "description": "Subscribe to NFL: http://j.mp/1L0bVBu Check out our other channels: Para más contenido de la NFL en Español, suscríbete a ...",
            "published_at": "2021-08-24T19:00:09Z",
            "created_at": "2021-08-24T21:38:12.114622Z",
            "thumbnails": {
                "high": {
                    "url": "https://i.ytimg.com/vi/IbFStMAXP58/hqdefault.jpg",
                    "width": 480,
                    "height": 360
                },
                "medium": {
                    "url": "https://i.ytimg.com/vi/IbFStMAXP58/mqdefault.jpg",
                    "width": 320,
                    "height": 180
                },
                "default": {
                    "url": "https://i.ytimg.com/vi/IbFStMAXP58/default.jpg",
                    "width": 120,
                    "height": 90
                }
            }
        }
    ]
}
```

2. Search API
```
curl --location --request GET 'localhost:8000/api/v1/video/search/?q=football&page_size=3'

{
    "next": "http://localhost:8000/api/v1/video/search/?cursor=bz0yJnA9MjAyMS0wOC0yNCsxOSUzQTU4JTNBMzElMkIwMCUzQTAw&page_size=3&q=football",
    "previous": null,
    "results": [
        {
            "id": 51,
            "video_source": "youtube",
            "title": "LIVE: Big Ten, ACC, Pac 12 Alliance is Official | 365 Sports | 8.24.21 | Big 12, SEC",
            "description": "Get your college football gear: https://fanatics.93n6tx.net/DVb0X2 Join David Smoak, Paul Catalina and Craig Smoak on 365 Sports Radio weekdays from 3-6 ...",
            "published_at": "2021-08-24T19:58:31Z",
            "created_at": "2021-08-24T20:38:00.743422Z",
            "thumbnails": {
                "high": {
                    "url": "https://i.ytimg.com/vi/tOjFB2cZDJ4/hqdefault_live.jpg",
                    "width": 480,
                    "height": 360
                },
                "medium": {
                    "url": "https://i.ytimg.com/vi/tOjFB2cZDJ4/mqdefault_live.jpg",
                    "width": 320,
                    "height": 180
                },
                "default": {
                    "url": "https://i.ytimg.com/vi/tOjFB2cZDJ4/default_live.jpg",
                    "width": 120,
                    "height": 90
                }
            }
        },
        {
            "id": 553,
            "video_source": "youtube",
            "title": "جربت أجدد وأقوى لعبة كورة على الموبايل !!! Vive le football",
            "description": "توا تجربة للعبة vive le football الجديدة على الموبايل فهل هي اسطوريه ام لا لا تنسى تشترك وتفعيل زر التنبيهات للأعلانات وللتواصل mistarufc@gmail.com تابعني ...",
            "published_at": "2021-08-24T16:32:03Z",
            "created_at": "2021-08-24T21:38:12.114786Z",
            "thumbnails": {
                "high": {
                    "url": "https://i.ytimg.com/vi/Z5ogrbJViXA/hqdefault.jpg",
                    "width": 480,
                    "height": 360
                },
                "medium": {
                    "url": "https://i.ytimg.com/vi/Z5ogrbJViXA/mqdefault.jpg",
                    "width": 320,
                    "height": 180
                },
                "default": {
                    "url": "https://i.ytimg.com/vi/Z5ogrbJViXA/default.jpg",
                    "width": 120,
                    "height": 90
                }
            }
        },
        {
            "id": 502,
            "video_source": "youtube",
            "title": "جربت أجدد وأقوى لعبة كورة على الموبايل !!! Vive le football",
            "description": "توا تجربة للعبة vive le football الجديدة على الموبايل فهل هي اسطوريه ام لا لا تنسى تشترك وتفعيل زر التنبيهات للأعلانات وللتواصل mistarufc@gmail.com تابعني ...",
            "published_at": "2021-08-24T16:32:03Z",
            "created_at": "2021-08-24T20:47:00.778062Z",
            "thumbnails": {
                "high": {
                    "url": "https://i.ytimg.com/vi/Z5ogrbJViXA/hqdefault.jpg",
                    "width": 480,
                    "height": 360
                },
                "medium": {
                    "url": "https://i.ytimg.com/vi/Z5ogrbJViXA/mqdefault.jpg",
                    "width": 320,
                    "height": 180
                },
                "default": {
                    "url": "https://i.ytimg.com/vi/Z5ogrbJViXA/default.jpg",
                    "width": 120,
                    "height": 90
                }
            }
        }
    ]
}

```
