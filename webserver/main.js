var app = angular.module("myApp", ["ngRoute"]);

app.config(function($routeProvider, $locationProvider) {
    $locationProvider.hashPrefix('');
    $locationProvider.html5Mode({
        enabled: true
    });
    
    $routeProvider
    	.when('/community', {
        	templateUrl: '../community.html'
        })
        .when('/home', {
        	templateUrl: '../home.html'
        })
        .when('/profile', {
        	templateUrl: '../profile.html'
        })
        .when('/signup', {
            templateUrl: '../signup.html'
        })
        .when('/userLogin', {
            templateUrl: '../userLogin.html'
        })
	.when('/user',{
		templateUrl: '../userLogin.html'
	})
        .otherwise({
            
        })
});
