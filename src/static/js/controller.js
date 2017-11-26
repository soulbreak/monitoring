var app = angular.module("myApp", ['routageModule','ApiModule','ApplicationModule','MenuModule']);


var ApiModule = angular.module('ApiModule',[])
    .service('dataservice', function($http) {
    this.getData = function() {
        return $http({
            method: 'GET',
            url: '/api/configuration'
         });
     }
});

var MenuModule = angular.module('MenuModule', [])
    .controller('MenuCtrl', ['$scope', function ($scope) {
      $scope.links = [
            { 'name' : 'configuration'},
            { 'name' : 'Statuses'},
            { 'name' : 'application'},
      ]}])
;

MenuModule.directive('menuDirective',function(){
    return {
        template : ' <a href="#!{{link.name}}">{{link.name}}</a>'
    }
})

var ApplicationModule = angular.module('ApplicationModule', ['ApiModule'])
    .controller("ConfigurationCtrl",
        [ '$scope',  'dataservice', function ($scope, dataservice) {

        $scope.data = null;
        $scope.get_configuration = function () {
            dataservice.getData().then(function(dataResponse) {
                $scope.data = dataResponse.data;
            });
        };

    }])
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
        }}])
    .directive("configurationDirective", function () {
        return {
            template: "{{ application.name }} {{ application.status }}"
        };
    })
;




