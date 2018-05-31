var app = angular.module("Scanner", ['webcam', 'bcQrReader']);

app.controller("scan-controller", function($scope, $http) {

    $scope.nuevas_asistencias = [];
    $scope.identificacion = "";
    $scope.start = function() {
      $scope.cameraRequested = true;
  }

  $scope.processURLfromQR = function (url) {
    $scope.url = url;
    $scope.cameraRequested = false;
    $scope.bien = false;
    $scope.mal = false;

    if($scope.url.length > 0){

        $http.defaults.xsrfCookieName = 'csrftoken';
        $http.defaults.xsrfHeaderName = 'X-CSRFToken';
        $scope.CurrentDate = new Date();
        $http.post("", $scope.url)
             .then(function (response) {
                 $scope.mal = true
                 if (response.status == 200) {
                     $scope.respuesta = response.data;
                     $scope.mensaje = $scope.respuesta["message"]
                     if($scope.respuesta["status"] == 200){
                         $scope.nuevas_asistencias.push(
                             {
                                 "documento": $scope.respuesta["asistencia"]["documento"],
                                 "nombre": $scope.respuesta["asistencia"]["nombre"],
                                 "fecha": $scope.respuesta["fecha"]
                             }
                             );
                         $scope.url = $scope.url.split("?",1)
                         $scope.mal = false
                         $scope.bien = true

                     }
                 }
             }, function(response){
              $scope.mal = true
                  $scope.mensaje = "Datos no existen"
             });
    }
  }

  $scope.asistenciaManual = function (id_curso) {
    $http.defaults.xsrfCookieName = 'csrftoken';
    $http.defaults.xsrfHeaderName = 'X-CSRFToken';

    $scope.bien = false;
    $scope.mal = false;

    var url = $scope.identificacion+"?"+id_curso
    $http.post("", url)
         .then(function (response) {
             $scope.mal = true
             if (response.status == 200) {
                 $scope.respuesta = response.data;
                 $scope.mensaje = $scope.respuesta["message"]
                 if($scope.respuesta["status"] == 200){
                     $scope.nuevas_asistencias.push(
                         {
                             "documento": $scope.respuesta["asistencia"]["documento"],
                             "nombre": $scope.respuesta["asistencia"]["nombre"],
                             "hora":  $scope.respuesta["fecha"],
                         }
                         );
                     $scope.bien = true
                     $scope.mal = false
                     $scope.identificacion = ""
                 }
             }
         }, function(response){
              $scope.mal = true
              $scope.mensaje = "Datos no existen"
         });

  }
});