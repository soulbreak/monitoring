var routageModule = angular.module('routageModule', ['ngRoute']);
routageModule .config(['$routeProvider', function ($routeProvider) {
    $routeProvider
    .when('/application', {
        templateUrl:  "/static/angular_templates/application.html",
        controller: "ApplicationCtrl"
    })
    .when('/configuration', {
        templateUrl:  "/static/angular_templates/configuration.html",
        controller: "ConfigurationCtrl"
    })
    .when('/index', {
        templateUrl:  "/static/angular_templates/index.html",
    })
    .when('/notfound', {
        templateUrl: "static/angular_templates/notfound.html",
    })
    .otherwise({
        redirectTo: '/notfound'
    })
}]);