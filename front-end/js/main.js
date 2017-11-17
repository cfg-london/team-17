var app = angular.module("myApp", ["firebase", "ngStorage", "ngRoute"]);
app.config(function($routeProvider, $locationProvider) {
    $locationProvider.hashPrefix('');
    $routeProvider
        .when('/', {
            templateUrl: '../templates/signup.html',
            controller: 'signup'
        })

});

app.controller("signup", ["$scope"
	function($scope) {
		$scope.user.name = ''
		
	}
]);