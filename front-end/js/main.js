var app = angular.module("myApp", ["ngRoute"]);

app.config(function($routeProvider, $locationProvider) {
    $locationProvider.hashPrefix('');
    $routeProvider
    	.when('/community', {
        	templateUrl: '../templates/community.html'
        })
        .when('/home', {
        	templateUrl: '../templates/home.html'
        })
        .when('/profile', {
        	templateUrl: '../templates/profile.html'
        })
        .when('/signup', {
            templateUrl: '../templates/signup.html'
        })
        .otherwise({
            templateUrl: '../templates/signup.html'
        })
});