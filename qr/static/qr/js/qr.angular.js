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
                         $scope.url = $scope.url.split("?",1)
                         if($scope.respuesta["status"] == 200){
                             $scope.nuevas_asistencias.push(
                                 {
                                     "documento": $scope.respuesta["asistencia"]["documento"],
                                     "nombre": $scope.respuesta["asistencia"]["nombre"],
                                     "fecha": $scope.respuesta["fecha"]
                                 }
                                 );
                             $scope.mal = false
                             $scope.bien = true
                         }
                     }
                 }, function(response){
                      $scope.mal = true
                      $scope.url = $scope.url.split("?",1)
                      $scope.mensaje = "No existe un registro con esa identificación en el sistema. Por favor comuniquese con el encargado si se trata de un error."
                 });
        }
  }

  $scope.asistenciaManual = function (id_curso) {
    $http.defaults.xsrfCookieName = 'csrftoken';
    $http.defaults.xsrfHeaderName = 'X-CSRFToken';
    $scope.bien = false;
    $scope.mal = false;

    $scope.url = $scope.identificacion+"?"+id_curso
    $http.post("", $scope.url)
         .then(function (response) {
             $scope.mal = true
             if (response.status == 200) {
                 $scope.respuesta = response.data;
                 $scope.mensaje = $scope.respuesta["message"]
                 $scope.url = $scope.url.split("?",1)
                 if($scope.respuesta["status"] == 200){
                     $scope.nuevas_asistencias.push(
                         {
                             "documento": $scope.respuesta["asistencia"]["documento"],
                             "nombre": $scope.respuesta["asistencia"]["nombre"],
                             "fecha":  $scope.respuesta["fecha"]
                         }
                         );
                     $scope.mal = false
                     $scope.bien = true
                     $scope.identificacion = ""
                 }
             }
         }, function(response){
              $scope.mal = true
              $scope.url = $scope.url.split("?",1)
              $scope.mensaje = "No existe un registro con esa identificación en el sistema. Por favor comuniquese con el encargado si se trata de un error."
         });

  }
});