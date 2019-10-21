This is a eazy Libray manager.
## 本项目是基于python,django,MySQL建立的网页版图书管理系统，可实现图书信息（书名，出版社，定价，零售价）的添加、更新、删除
### 使用方法
- 1 创建数据库
  - 1.1 在本机创建MySQL数据库，命名为mysite4;
  - 1.2 迁移数据　在mysite4目录下 
  ```python
  python3 manage.py makemigrations
  python3 manage.py migrate
  ```
- 2.运行服务端
  ```python
  python3 manage.py runserver
  ```
- 3.打开网页图书管理系统
  ```html
  http://127.0.0.1:8000/all_book
  ```
