class Article {
  late String title;
  late String description;
  late String url;
  late String urlToImage;

  Article({
    this.title = "Title",
    this.description = "Description",
    this.url = "Some Url",
    this.urlToImage = "Some Url",
  });

  factory Article.fromMap(Map news) {
    return Article(
      title: news["title"],
      description: news["description"] ?? "Na",
      url: news["url"],
      urlToImage: news["urlToImage"] ?? "https://images.unsplash.com/photo-1586339949916-3e9457bef6d3?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80",
    );
  }
}
