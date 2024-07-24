### 短网址生成器

#### 创建数据库及表

##### 创建数据库：
创建一个 app 库。
```mysql
create database app;
```

##### 创建表：
创建一张tiny_urls表。
```mysql
CREATE TABLE `tiny_urls` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `original_url` text NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
```

#### 运行项目
运行app.py，启动项目。
```python
python app.py
```

##### 访问
启动后，访问 http://127.0.0.1:8001/index.html 