// Generated by CoffeeScript 1.6.3
(function() {
  var _ref,
    __hasProp = {}.hasOwnProperty,
    __extends = function(child, parent) { for (var key in parent) { if (__hasProp.call(parent, key)) child[key] = parent[key]; } function ctor() { this.constructor = child; } ctor.prototype = parent.prototype; child.prototype = new ctor(); child.__super__ = parent.prototype; return child; };

  if (typeof Backbone !== "undefined" && Backbone !== null) {
    this.NewPostInlineView = (function(_super) {
      __extends(NewPostInlineView, _super);

      function NewPostInlineView() {
        _ref = NewPostInlineView.__super__.constructor.apply(this, arguments);
        return _ref;
      }

      NewPostInlineView.prototype.initialize = function() {
        this.topicId = this.$(".topic").first().data("discussion-id");
        this.maxNameWidth = 100;
        return DiscussionUtil.makeWmdEditor(this.$el, $.proxy(this.$, this), "new-post-body");
      };

      NewPostInlineView.prototype.events = {
        "submit .new-post-form": "createPost"
      };

      NewPostInlineView.prototype.ignoreClick = function(event) {
        return event.stopPropagation();
      };

      NewPostInlineView.prototype.createPost = function(event) {
        var anonymous, anonymous_to_peers, body, follow, group, title, url,
          _this = this;
        event.preventDefault();
        title = this.$(".new-post-title").val();
        body = this.$(".new-post-body").find(".wmd-input").val();
        group = this.$(".new-post-group option:selected").attr("value");
        anonymous = false || this.$("input.discussion-anonymous").is(":checked");
        anonymous_to_peers = false || this.$("input.discussion-anonymous-to-peers").is(":checked");
        follow = false || this.$("input.discussion-follow").is(":checked");
        url = DiscussionUtil.urlFor('create_thread', this.topicId);
        return DiscussionUtil.safeAjax({
          $elem: $(event.target),
          $loading: event ? $(event.target) : void 0,
          url: url,
          type: "POST",
          dataType: 'json',
          async: false,
          data: {
            title: title,
            body: body,
            group_id: group,
            anonymous: anonymous,
            anonymous_to_peers: anonymous_to_peers,
            auto_subscribe: follow
          },
          error: DiscussionUtil.formErrorHandler(this.$(".new-post-form-errors")),
          success: function(response, textStatus) {
            var thread;
            thread = new Thread(response['content']);
            DiscussionUtil.clearFormErrors(_this.$(".new-post-form-errors"));
            _this.$el.hide();
            _this.$(".new-post-title").val("").attr("prev-text", "");
            _this.$(".new-post-body textarea").val("").attr("prev-text", "");
            return _this.collection.add(thread);
          }
        });
      };

      return NewPostInlineView;

    })(Backbone.View);
  }

}).call(this);
