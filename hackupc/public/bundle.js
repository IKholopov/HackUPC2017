/******/ (function(modules) { // webpackBootstrap
/******/ 	// The module cache
/******/ 	var installedModules = {};

/******/ 	// The require function
/******/ 	function __webpack_require__(moduleId) {

/******/ 		// Check if module is in cache
/******/ 		if(installedModules[moduleId])
/******/ 			return installedModules[moduleId].exports;

/******/ 		// Create a new module (and put it into the cache)
/******/ 		var module = installedModules[moduleId] = {
/******/ 			i: moduleId,
/******/ 			l: false,
/******/ 			exports: {}
/******/ 		};

/******/ 		// Execute the module function
/******/ 		modules[moduleId].call(module.exports, module, module.exports, __webpack_require__);

/******/ 		// Flag the module as loaded
/******/ 		module.l = true;

/******/ 		// Return the exports of the module
/******/ 		return module.exports;
/******/ 	}


/******/ 	// expose the modules object (__webpack_modules__)
/******/ 	__webpack_require__.m = modules;

/******/ 	// expose the module cache
/******/ 	__webpack_require__.c = installedModules;

/******/ 	// identity function for calling harmony imports with the correct context
/******/ 	__webpack_require__.i = function(value) { return value; };

/******/ 	// define getter function for harmony exports
/******/ 	__webpack_require__.d = function(exports, name, getter) {
/******/ 		if(!__webpack_require__.o(exports, name)) {
/******/ 			Object.defineProperty(exports, name, {
/******/ 				configurable: false,
/******/ 				enumerable: true,
/******/ 				get: getter
/******/ 			});
/******/ 		}
/******/ 	};

/******/ 	// getDefaultExport function for compatibility with non-harmony modules
/******/ 	__webpack_require__.n = function(module) {
/******/ 		var getter = module && module.__esModule ?
/******/ 			function getDefault() { return module['default']; } :
/******/ 			function getModuleExports() { return module; };
/******/ 		__webpack_require__.d(getter, 'a', getter);
/******/ 		return getter;
/******/ 	};

/******/ 	// Object.prototype.hasOwnProperty.call
/******/ 	__webpack_require__.o = function(object, property) { return Object.prototype.hasOwnProperty.call(object, property); };

/******/ 	// __webpack_public_path__
/******/ 	__webpack_require__.p = "";

/******/ 	// Load entry module and return exports
/******/ 	return __webpack_require__(__webpack_require__.s = 0);
/******/ })
/************************************************************************/
/******/ ([
/* 0 */
/***/ (function(module, exports) {

throw new Error("Module build failed: Error: The node API for `babel` has been moved to `babel-core`.\n    at Object.<anonymous> (/home/zerts/MIPT/hackUPC/HackUPC2017/hackupc/node_modules/babel/index.js:1:69)\n    at Module._compile (module.js:410:26)\n    at Object.Module._extensions..js (module.js:417:10)\n    at Module.load (module.js:344:32)\n    at Function.Module._load (module.js:301:12)\n    at Module.require (module.js:354:17)\n    at require (internal/module.js:12:17)\n    at loadLoader (/home/zerts/MIPT/hackUPC/HackUPC2017/hackupc/node_modules/loader-runner/lib/loadLoader.js:13:17)\n    at iteratePitchingLoaders (/home/zerts/MIPT/hackUPC/HackUPC2017/hackupc/node_modules/loader-runner/lib/LoaderRunner.js:169:2)\n    at runLoaders (/home/zerts/MIPT/hackUPC/HackUPC2017/hackupc/node_modules/loader-runner/lib/LoaderRunner.js:362:2)\n    at NormalModule.doBuild (/home/zerts/MIPT/hackUPC/HackUPC2017/hackupc/node_modules/webpack/lib/NormalModule.js:129:2)\n    at NormalModule.build (/home/zerts/MIPT/hackUPC/HackUPC2017/hackupc/node_modules/webpack/lib/NormalModule.js:180:15)\n    at Compilation.buildModule (/home/zerts/MIPT/hackUPC/HackUPC2017/hackupc/node_modules/webpack/lib/Compilation.js:142:10)\n    at /home/zerts/MIPT/hackUPC/HackUPC2017/hackupc/node_modules/webpack/lib/Compilation.js:424:9\n    at /home/zerts/MIPT/hackUPC/HackUPC2017/hackupc/node_modules/webpack/lib/NormalModuleFactory.js:242:4\n    at /home/zerts/MIPT/hackUPC/HackUPC2017/hackupc/node_modules/webpack/lib/NormalModuleFactory.js:93:13\n    at /home/zerts/MIPT/hackUPC/HackUPC2017/hackupc/node_modules/tapable/lib/Tapable.js:204:11\n    at NormalModuleFactory.<anonymous> (/home/zerts/MIPT/hackUPC/HackUPC2017/hackupc/node_modules/webpack/lib/CompatibilityPlugin.js:52:5)\n    at NormalModuleFactory.applyPluginsAsyncWaterfall (/home/zerts/MIPT/hackUPC/HackUPC2017/hackupc/node_modules/tapable/lib/Tapable.js:208:13)\n    at onDoneResolving (/home/zerts/MIPT/hackUPC/HackUPC2017/hackupc/node_modules/webpack/lib/NormalModuleFactory.js:68:11)\n    at onDoneResolving (/home/zerts/MIPT/hackUPC/HackUPC2017/hackupc/node_modules/webpack/lib/NormalModuleFactory.js:189:6)\n    at nextTickCallbackWith0Args (node.js:419:9)\n    at process._tickCallback (node.js:348:13)");

/***/ })
/******/ ]);