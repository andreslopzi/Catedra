var app = angular.module("Scanner", ['webcam', 'bcQrReader']);


app.controller("scan-controller", function($scope, $http) {
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
                if(response.status == 200){
                    //alert("Asistencias tomada con exito");
                    $scope.respuesta = response.data;
                    $scope.mensaje = $scope.respuesta["message"]
                }
                else{
                    $scope.mensaje = "Error"
                    console.log(response.status)
                }
             });

    }
  }

});