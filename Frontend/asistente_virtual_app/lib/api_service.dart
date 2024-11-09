import 'dart:convert';
import 'package:http/http.dart' as http;
import 'package:shared_preferences/shared_preferences.dart';

class ApiService {
  final String baseUrl = "http://127.0.0.1:8000/api";

  // Método para iniciar sesión
  Future<void> login(String username, String password) async {
    final response = await http.post(
      Uri.parse("$baseUrl/token/"),
      headers: {"Content-Type": "application/json"},
      body: json.encode({"username": username, "password": password}),
    );

    if (response.statusCode == 200) {
      final data = json.decode(response.body);
      SharedPreferences prefs = await SharedPreferences.getInstance();
      await prefs.setString('access_token', data['access']);
      await prefs.setString('refresh_token', data['refresh']); // Guardar refresh token
    } else {
      throw Exception("Fallo en el inicio de sesión. Código de estado: ${response.statusCode}");
    }
  }

  // Método para obtener usuarios (requiere autenticación)
  Future<List> getUsuarios() async {
    SharedPreferences prefs = await SharedPreferences.getInstance();
    String? token = prefs.getString('access_token');

    if (token == null) {
      throw Exception("No hay token de acceso almacenado");
    }

    final response = await http.get(
      Uri.parse("$baseUrl/usuarios/"),
      headers: {
        "Content-Type": "application/json",
        "Authorization": "Bearer $token",
      },
    );

    if (response.statusCode == 200) {
      return json.decode(response.body);
    } else {
      throw Exception("Fallo al cargar usuarios. Código de estado: ${response.statusCode}");
    }
  }
  Future<void> registrarUsuario(String username, String email, String password) async {
  final response = await http.post(
    Uri.parse("$baseUrl/registro/"),
    headers: {"Content-Type": "application/json"},
    body: json.encode({"username": username, "password": password, "email": email}),
  );

  if (response.statusCode != 201) {
    throw Exception("Fallo al registrar usuario. Código de estado: ${response.statusCode}");
  }
}

}
