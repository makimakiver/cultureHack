import 'package:flutter/material.dart';
import 'package:flutter_earth_globe/flutter_earth_globe.dart';
import 'package:flutter_earth_globe/flutter_earth_globe_controller.dart';
import 'package:flutter_earth_globe/globe_coordinates.dart';
import 'package:flutter_earth_globe/point.dart';
import 'package:hackathon/models/coodinate.dart';



class Globe extends StatelessWidget {
late FlutterEarthGlobeController _controller;

@override
initState() {
  _controller = FlutterEarthGlobeController(
      rotationSpeed: 0.05,
      isBackgroundFollowingSphereRotation: true,
    background: AssetImage("assets/night.jpg"),
      surface: NetworkImage("assets/world_map.gif")
  );




}

@override
Widget build(BuildContext context) {
  initState();
  List<Point> points = [


    Point(
        id: '1',
        isLabelVisible: true,
        coordinates: const GlobeCoordinates(5.6895, 130.6917), // 35.6764° N, 139.6500° E
        style: const PointStyle(color: Colors.blue),

        onTap: (){
          Coordinate cord = Coordinate(5.6895, 130.6917);
          print(cord.getLatitude());
          print(cord.getLongitude());
        },
        label: 'region1'),

    Point(
        id: '2',
        isLabelVisible: true,
        coordinates: const GlobeCoordinates(43.0618 - 30, 141.3545 - 9), // 43.0618° N, 141.3545° E - 30, - 9
        style: const PointStyle(color: Colors.blue),

        onTap: (){
          Coordinate cord = Coordinate(43.0618 - 30, 141.3545 - 9);
          print(cord.getLatitude());
          print(cord.getLongitude());
        },
        label: 'region2'),

    Point(
        id: '3',
        isLabelVisible: true,
        coordinates: const GlobeCoordinates(32.7503 - 30, 129.8779 - 9), // 32.7503° N, 129.8779
        style: const PointStyle(color: Colors.blue),

        onTap: (){
          Coordinate cord = Coordinate(32.7503 - 30, 129.8779 - 9);
          print(cord.getLatitude());
          print(cord.getLongitude());
        },
        label: 'region3'),





    Point(
        id: '40',
        isLabelVisible: true,
        onTap: () {
          Future.delayed(Duration.zero, () {
            showDialog(
                context: context,
                builder: (context) => const AlertDialog(
                  title: Text('Center'),
                  content: Text('This is the center of the globe'),
                ));
          });
        },
        coordinates: const GlobeCoordinates(0, 0),
        style: const PointStyle(color: Colors.yellow),
        label: 'Center'),
  ];

  for (var point in points) {
    _controller.addPoint(point);
  }
  return MaterialApp(
    home: Scaffold(
      appBar: AppBar(
        title: Text('Flutter Global Earth'),
      ),
      body: SafeArea(
          child: FlutterEarthGlobe(
            controller: _controller,
            radius: 120,
          )
      ),
    ),
  );
}
}