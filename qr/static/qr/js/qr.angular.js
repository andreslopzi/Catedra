var app = angular.module("Scanner", ['webcam', 'bcQrReader']);


app.controller("scan-controller", function($scope, $http) {

    $scope.nuevas_asistencias = [];

    $scope.start = function() {
      $scope.cameraRequested = true;
  }

  $scope.processURLfromQR = function (url) {
    $scope.url = url;
    $scope.cameraRequested = false;

    if($scope.url.length > 0){

        $http.defaults.xsrfCookieName = 'csrftoken';
        $http.defaults.xsrfHeaderName = 'X-CSRFToken';

        $http.post("", $scope.url)
             .then(function (response) {
                 if (response.status == 200) {
                     $scope.respuesta = response.data;
                     $scope.mensaje = $scope.respuesta["message"]
                     if($scope.respuesta["status"] == 200){
                         $scope.nuevas_asistencias.push(
                             {
                                 "documento": $scope.respuesta["asistencia"]["documento"],
                                 "nombre": $scope.respuesta["asistencia"]["nombre"],
                                 "hora": "1 de la manana",
                             }
                             );
                     }
                 }
                 alert($scope.nuevas_asistencias);
             }, function(response){
                  $scope.mensaje = "Datos no existen"
             });
    }
  }

});