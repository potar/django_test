
/* Project specific Javascript goes here. */

angular.module('dynamic_models.controllers', [])

    .controller('usersController', function($scope, usersService, xeditableService) {
        $scope.settings = DYNAMIC_MODELS_APP_SETTINGS
        $scope.users = [];
        usersService.get_users().success(function(response) {
           $scope.users = response;
        });

        $scope.intValidator = xeditableService.intValidator;
        $scope.updateData = xeditableService.updateData;

        $scope.submitForm = function(is_valid) {
            if (is_valid) {
                var new_user = angular.copy(this.form)
                this.users.push(new_user);
                //TODO: send data to a server
            }
        }
    })

    .controller('roomsController', function($scope, roomsService, xeditableService) {
        $scope.settings = DYNAMIC_MODELS_APP_SETTINGS
        $scope.rooms = [];
        roomsService.get_rooms().success(function(response) {
           $scope.rooms = response;
        });

        $scope.intValidator = xeditableService.intValidator;
        $scope.updateData = xeditableService.updateData;

        $scope.submitForm = function(is_valid) {
            if (is_valid) {
                var new_room = angular.copy(this.form)
                this.rooms.push(new_room);
                //TODO: send data to a server
            }
        }
    });


angular.module('dynamic_models.services', [])
    .factory('usersService', function($http) {
        var api = {};
        api.get_users = function() {
            return $http.get(
                DYNAMIC_MODELS_APP_SETTINGS.list_users,
                {'headers': {'X_REQUESTED_WITH': 'XMLHttpRequest'}}
            );
        }
        return api;
    })
    .factory('roomsService', function($http) {
        var api = {};
        api.get_rooms = function() {
            return $http.get(
                DYNAMIC_MODELS_APP_SETTINGS.list_rooms,
                {'headers': {'X_REQUESTED_WITH': 'XMLHttpRequest'}}
            );
        }
        return api;
    })
    .factory('xeditableService', function($http) {
        var api = {};
        api.intValidator = function(data) {
            if (!/^\d+$/.test(data)){
               return "You can enter only digits."
            }
        }
        api.updateData = function(url, data, field_name) {
            var obj = {};
            obj['id'] = data['id'];
            obj[field_name] = data[field_name];
            return $http.post(url, obj)
        }
        return api
    });

angular.module('dynamic_models', [
  'dynamic_models.controllers',
  'dynamic_models.services',
  'xeditable',
  'ui.bootstrap',
  'ngRoute',
]).config(['$routeProvider', function($routeProvider){
    $routeProvider
        .when("/users", {templateUrl: DYNAMIC_MODELS_APP_SETTINGS.users_partial_view, controller: "usersController"})
        .when("/rooms", {templateUrl: DYNAMIC_MODELS_APP_SETTINGS.rooms_partial_view, controller: "roomsController"})
        .otherwise({redirectTo: '/users'});
}]).run(function(editableOptions) {
      editableOptions.theme = 'bs3'; // bootstrap3 theme. Can be also 'bs2', 'default'
})
