가상환경 생성 : python -m venv venv



가상환경 실행 : source venv/Scripts/activate



장고 설치 : pip install django==3.2.12



프로젝트 생성 : django-admin startproject 프로젝트명 .



서버 실행 : python manage.py runserver



초기 설정 변경 : 프로젝트 폴더 안 settings.py에서 LANGUAGE_CODE, TIME_ZONE 등 변경



앱 생성 : python manage.py startapp articles

​				settings.py의 INSTALLED_APPS에서 'articles' 추가

​				urls 에서 from articles import views







.gitignore

git : 해당 저장소가 있는 폴더의 모든 파일의 변경 사항을 추적

폴더 중에서 특정 파일/폴더/확장자 git으로 관리하고 싶지 않다



나중에 제대로 정리 예정