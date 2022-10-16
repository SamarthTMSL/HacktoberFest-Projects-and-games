import 'dart:convert';

import 'package:http/http.dart' as http;

import '../model/article.dart';

class Worker {
  String location;
  String? category;
  List<Article> articles = [];
  List<Article> articlesForCarousel = [];

  Worker({
    required this.location,
    this.category = "Na",
  });

  Future<List<Article>> getArticles() async {
    var url;
    if (category == "Na") {
      url = Uri.parse(
          "https://newsapi.org/v2/top-headlines?country=$location&apiKey=bfa65db373914f89b072543a7ac883d3");
    } else if (category == "corona") {
      url = Uri.parse(
          "https://newsapi.org/v2/everything?q=coronavirus&language=en&from=2022-05-30&sortBy=publishedAt&apiKey=bfa65db373914f89b072543a7ac883d3");
    } else {
      url = Uri.parse(
          "https://newsapi.org/v2/top-headlines?country=$location&category=$category&apiKey=bfa65db373914f89b072543a7ac883d3");
    }
    final response = await http.get(url);
    Map data = json.decode(response.body);
    final articleMap = data["articles"];
    articleMap.forEach((article) {
      Article newArticle = Article();
      newArticle = Article.fromMap(article);
      articles.add(newArticle);
    });
    return articles;
  }

  Future<List<Article>> getArticlesForCarousel() async {
    final url = Uri.parse(
        "https://newsapi.org/v2/everything?q=india&from=2022-06-1&sortBy=publishedAt&language=en&apiKey=bfa65db373914f89b072543a7ac883d3");
    final response = await http.get(url);
    Map data = json.decode(response.body);
    final articleMap = data["articles"];
    print(data);
    print("Article Map is above");
    for (var i = 0; i < 4; i++) {
      Article newArticle = Article();
      newArticle = Article.fromMap(articleMap[i]);
      articlesForCarousel.add(newArticle);
    }
    return articlesForCarousel;
  }
}
