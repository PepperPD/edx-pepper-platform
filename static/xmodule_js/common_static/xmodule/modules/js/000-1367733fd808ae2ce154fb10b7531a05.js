// Generated by CoffeeScript 1.6.3
(function() {
  var __bind = function(fn, me){ return function(){ return fn.apply(me, arguments); }; };

  this.XModule = {
    /*
    Load a single module (either an edit module or a display module)
    from the supplied element, which should have a data-type attribute
    specifying the class to load
    */

    loadModule: function(element) {
      var error, module, moduleType;
      moduleType = $(element).data('type');
      if (moduleType === 'None') {
        return;
      }
      try {
        module = new window[moduleType](element);
        if ($(element).hasClass('xmodule_edit')) {
          $(document).trigger('XModule.loaded.edit', [element, module]);
        }
        if ($(element).hasClass('xmodule_display')) {
          $(document).trigger('XModule.loaded.display', [element, module]);
        }
        return module;
      } catch (_error) {
        error = _error;
        if (window.console && console.log) {
          return console.error("Unable to load " + moduleType + ": " + error.message);
        } else {
          throw error;
        }
      }
    },
    /*
    Load all modules on the page of the specified type.
    If container is provided, only load modules inside that element
    Type is one of 'display' or 'edit'
    */

    loadModules: function(container) {
      var modules, selector;
      selector = ".xmodule_edit, .xmodule_display";
      if (container != null) {
        modules = $(container).find(selector);
      } else {
        modules = $(selector);
      }
      return modules.each(function(idx, element) {
        return XModule.loadModule(element);
      });
    }
  };

  this.XModule.Descriptor = (function() {
    /*
    Register a callback method to be called when the state of this
    descriptor is updated. The callback will be passed the results
    of calling the save method on this descriptor.
    */

    Descriptor.prototype.onUpdate = function(callback) {
      if (this.callbacks == null) {
        this.callbacks = [];
      }
      return this.callbacks.push(callback);
    };

    /*
    Notify registered callbacks that the state of this descriptor has changed
    */


    Descriptor.prototype.update = function() {
      var callback, data, _i, _len, _ref, _results;
      data = this.save();
      _ref = this.callbacks;
      _results = [];
      for (_i = 0, _len = _ref.length; _i < _len; _i++) {
        callback = _ref[_i];
        _results.push(callback(data));
      }
      return _results;
    };

    /*
    Bind the module to an element. This may be called multiple times,
    if the element content has changed and so the module needs to be rebound
    
    @method: constructor
    @param {html element} the .xmodule_edit section containing all of the descriptor content
    */


    function Descriptor(element) {
      this.element = element;
      this.update = __bind(this.update, this);
      return;
    }

    /*
    Return the current state of the descriptor (to be written to the module store)
    
    @method: save
    @returns {object} An object containing children and data attributes (both optional).
                      The contents of the attributes will be saved to the server
    */


    Descriptor.prototype.save = function() {
      return {};
    };

    return Descriptor;

  })();

}).call(this);
