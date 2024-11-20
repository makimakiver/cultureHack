class Coordinate{
  late double longitude;
  late double latitude;

  Coordinate(double long, double lat){
    longitude = long + 30;
    latitude = lat + 9;
  }

  double getLongitude(){
    return longitude;
  }

  double getLatitude(){
    return latitude;
  }

  // 35.6764° N, 139.6500° E
}