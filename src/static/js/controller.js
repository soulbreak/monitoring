var app = angular.module("myApp", ['ApplicationModule','MenuModule']);



var MenuModule = angular.module('MenuModule', []);


MenuModule.controller('MenuCtrl', ['$scope', function ($scope) {
      $scope.links = [
          { 'name' : 'Configuration'},
          { 'name' : 'Statuses'}
      ]
}]);


MenuModule.directive('menuDirective',function(){
    return {
        template : '{{link.name}}'
    }
})

var ApplicationModule = angular.module('ApplicationModule', [])
    .controller("ApplicationCtrl", [ '$scope', 'ApplicationService', function ($scope, ApplicationService) {
        $scope.applications = [{
                'name' : 'applicationA',
                'status' : 'up'
            },
            {
                'name': 'applicationB',
                'status': 'down'
            }
        ]
    $scope.select_application = function (application) {
        ApplicationService.select_application(application);
    };

    }])
    .controller("SelectedCtrl", [ '$scope', 'ApplicationService', function ($scope, ApplicationService) {
        $scope.selected = ApplicationService.selected;
    }])
    .service("ApplicationService", [function () {
        this.selected = [];

        this.select_application = function (application) {
            console.log('push');
            this.selected.push(application);
        };
}]);




ApplicationModule.directive("configurationDirective", function () {
    return {
        template: "{{ application.name }} {{ application.status }}"
    };
})

