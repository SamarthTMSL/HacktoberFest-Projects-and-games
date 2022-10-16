import 'dart:io';

import 'package:flutter/material.dart';
import 'package:webview_flutter/webview_flutter.dart';

class ArticleScreen extends StatefulWidget {
  static const routeName = "/article-page";
  const ArticleScreen({
    Key? key,
  }) : super(key: key);

  @override
  State<ArticleScreen> createState() => _ArticleScreenState();
}

class _ArticleScreenState extends State<ArticleScreen> {
  @override
  void initState() {
    // TODO: implement initState
    super.initState();
    if (Platform.isAndroid) WebView.platform = AndroidWebView();
  }
  @override
  Widget build(BuildContext context) {
    String url = ModalRoute.of(context)!.settings.arguments as String;
    return Scaffold(
      appBar: AppBar(
        elevation: 0,
        leading: const BackButton(
          color: Colors.black,
        ),
        backgroundColor: Colors.white,
      ),
      body: WebView(
        initialUrl: url,
        javascriptMode: JavascriptMode.unrestricted,
      ),
    );
  }
}
