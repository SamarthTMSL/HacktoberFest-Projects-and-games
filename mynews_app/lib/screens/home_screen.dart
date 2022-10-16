import 'package:carousel_slider/carousel_slider.dart';
import 'package:flutter/material.dart';
import 'package:mynews_app/screens/article_screen.dart';

import '../model/article.dart';
import '../worker/worker.dart';

class HomeScreen extends StatefulWidget {
  const HomeScreen({Key? key}) : super(key: key);

  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  int _currentIndex = 0;
  bool _isLoading = false;

  List navBarItem = [
    "All News",
    "Business",
    "Entertainment",
    "Technology",
    "Covid-19",
    "Sports",
  ];
  List categoryForNavBarItems = [
    "na",
    "business",
    "entertainment",
    "technology",
    "corona",
    "sports",
  ];
  List<bool> buttons = [true, false, false, false, false, false];
  List<Article> articles = [];
  List<Article> articlesForCarousel = [];
  void startApp(String category) async {
    _isLoading = true;
    late Worker worker;
    if (category == "na") {
      worker = Worker(location: "in");
      articles = await worker.getArticles();
    } else {
      worker = Worker(location: "in", category: category);
      articles = await worker.getArticles();
    }
    articlesForCarousel = await worker.getArticlesForCarousel();
    _isLoading = false;
    // print(articlesForCarousel);
    setState(() {});
  }

  @override
  void initState() {
    // TODO: implement initState
    super.initState();
    startApp("na");
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.white,
      appBar: AppBar(
        centerTitle: true,
        elevation: 0,
        backgroundColor: Colors.white,
        title: Row(
          mainAxisAlignment: MainAxisAlignment.center,
          children: const [
            Text(
              "India",
              style: TextStyle(
                color: Colors.black,
                fontWeight: FontWeight.bold,
              ),
            ),
            Text(
              "News",
              style: TextStyle(
                color: Colors.orange,
                fontWeight: FontWeight.bold,
              ),
            ),
          ],
        ),
      ),
      body: (_isLoading)
          ? const Center(
              child: CircularProgressIndicator(
                color: Colors.orange,
              ),
            )
          : SingleChildScrollView(
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Container(
                    // color: Colors.amber,
                    height: 58,
                    child: ListView.builder(
                      itemBuilder: (context, index) {
                        return Container(
                          padding: const EdgeInsets.all(8),
                          margin: const EdgeInsets.all(4),
                          child: InkWell(
                            onTap: () {
                              setState(() {
                                buttons = [
                                  false,
                                  false,
                                  false,
                                  false,
                                  false,
                                  false
                                ];
                                buttons[index] = true;
                                startApp(categoryForNavBarItems[index]);
                              });
                            },
                            child: Container(
                              // padding: const EdgeInsets.only(bottom: 5),
                              decoration: (buttons[index])
                                  ? const BoxDecoration(
                                      border: Border(
                                        bottom: BorderSide(
                                          color: Colors.orange,
                                          width: 3,
                                        ),
                                      ),
                                    )
                                  : const BoxDecoration(),
                              child: Text(
                                navBarItem[index],
                                style: TextStyle(
                                  fontSize: 17,
                                  color: Colors.grey[800],

                                  // fontWeight: FontWeight.bold,
                                ),
                              ),
                            ),
                          ),
                        );
                      },
                      itemCount: navBarItem.length,
                      scrollDirection: Axis.horizontal,
                    ),
                  ),
                  CarouselSlider(
                    options: CarouselOptions(
                      autoPlay: true,
                      onPageChanged: (index, reason) {
                        setState(
                          () {
                            _currentIndex = index;
                          },
                        );
                      },
                    ),
                    items: articlesForCarousel
                        .map(
                          (item) => Padding(
                            padding: const EdgeInsets.all(8.0),
                            child: InkWell(
                              onTap: () {
                                Navigator.of(context).pushNamed(
                                    ArticleScreen.routeName,
                                    arguments:
                                        articlesForCarousel[_currentIndex].url);
                              },
                              child: Card(
                                margin: const EdgeInsets.only(
                                  top: 10.0,
                                  bottom: 10.0,
                                ),
                                elevation: 6.0,
                                shadowColor: Colors.orange,
                                shape: RoundedRectangleBorder(
                                  borderRadius: BorderRadius.circular(15.0),
                                ),
                                child: ClipRRect(
                                  borderRadius: const BorderRadius.all(
                                    Radius.circular(15.0),
                                  ),
                                  child: Stack(
                                    children: <Widget>[
                                      Image.network(
                                        item.urlToImage,
                                        fit: BoxFit.cover,
                                        width: double.infinity,
                                        height: double.infinity,
                                        errorBuilder:
                                            (context, exception, stackTrace) {
                                          return Text('Your error widget...');
                                        },
                                      ),
                                      Positioned(
                                        left: 0,
                                        right: 0,
                                        bottom: 0,
                                        child: Container(
                                          padding: const EdgeInsets.all(8),
                                          decoration: BoxDecoration(
                                            gradient: LinearGradient(
                                              colors: [
                                                Colors.black12.withOpacity(0),
                                                Colors.black,
                                              ],
                                              begin: Alignment.topCenter,
                                              end: Alignment.bottomCenter,
                                            ),
                                          ),
                                          child: Text(
                                            item.title,
                                            style: const TextStyle(
                                              fontSize: 17.0,
                                              fontWeight: FontWeight.bold,
                                              color: Colors.white,
                                            ),
                                          ),
                                        ),
                                      ),
                                    ],
                                  ),
                                ),
                              ),
                            ),
                          ),
                        )
                        .toList(),
                  ),
                  Row(
                    mainAxisAlignment: MainAxisAlignment.center,
                    children: articlesForCarousel.map((urlOfItem) {
                      int index = articlesForCarousel.indexOf(urlOfItem);
                      return Container(
                        width: 10.0,
                        height: 10.0,
                        margin: const EdgeInsets.symmetric(
                            vertical: 10.0, horizontal: 2.0),
                        decoration: BoxDecoration(
                          shape: BoxShape.circle,
                          color: _currentIndex == index
                              ? const Color.fromARGB(204, 245, 133, 4)
                              : const Color.fromARGB(73, 14, 13, 13),
                        ),
                      );
                    }).toList(),
                  ),
                  const Padding(
                    padding: EdgeInsets.all(20.0),
                    child: Text(
                      "Latest news",
                      style: TextStyle(
                        fontSize: 25,
                        fontWeight: FontWeight.bold,
                      ),
                    ),
                  ),
                  ListView.builder(
                    physics: const ScrollPhysics(),
                    shrinkWrap: true,
                    itemBuilder: (context, index) {
                      return Container(
                        margin: const EdgeInsets.all(8),
                        child: InkWell(
                          onTap: () {
                            Navigator.of(context).pushNamed(
                                ArticleScreen.routeName,
                                arguments: articles[index].url);
                          },
                          child: Card(
                            elevation: 8,
                            child: Row(
                              children: [
                                ClipRRect(
                                  borderRadius: BorderRadius.circular(6),
                                  child: Image.network(
                                    articles[index].urlToImage,
                                    width: 150,
                                  ),
                                ),
                                Flexible(
                                  child: Container(
                                    margin: const EdgeInsets.only(left: 20),
                                    width: 200,
                                    child: Text(
                                      articles[index].title,
                                      style: const TextStyle(
                                        fontSize: 16,
                                        fontWeight: FontWeight.bold,
                                      ),
                                    ),
                                  ),
                                ),
                              ],
                            ),
                          ),
                        ),
                      );
                    },
                    itemCount: articles.length,
                  ),
                ],
              ),
            ),
    );
  }
}
