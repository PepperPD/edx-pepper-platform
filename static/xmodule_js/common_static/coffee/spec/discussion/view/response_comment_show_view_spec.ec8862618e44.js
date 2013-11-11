// Generated by CoffeeScript 1.6.3
(function() {
  describe('ResponseCommentShowView', function() {
    beforeEach(function() {
      setFixtures("<ol class=\"responses\"></ol>\n<script id=\"response-comment-show-template\" type=\"text/template\">\n    <div id=\"comment_<%- id %>\">\n    <div class=\"response-body\"><%- body %></div>\n    <div class=\"discussion-flag-abuse notflagged\" data-role=\"thread-flag\" data-tooltip=\"report misuse\">\n    <i class=\"icon\"></i><span class=\"flag-label\"></span></div>\n    <p class=\"posted-details\">&ndash;posted <span class=\"timeago\" title=\"<%- created_at %>\"><%- created_at %></span> by\n    <% if (obj.username) { %>\n    <a href=\"<%- user_url %>\" class=\"profile-link\"><%- username %></a>\n    <% } else {print('anonymous');} %>\n    </p>\n    </div>\n</script>");
      this.response = new Comment({
        id: '01234567',
        user_id: '567',
        course_id: 'mitX/999/test',
        body: 'this is a response',
        created_at: '2013-04-03T20:08:39Z',
        abuse_flaggers: ['123'],
        roles: []
      });
      return this.view = new ResponseCommentShowView({
        model: this.response
      });
    });
    it('defines the tag', function() {
      expect($('#jasmine-fixtures')).toExist;
      expect(this.view.tagName).toBeDefined;
      return expect(this.view.el.tagName.toLowerCase()).toBe('li');
    });
    it('is tied to the model', function() {
      return expect(this.view.model).toBeDefined();
    });
    return describe('rendering', function() {
      beforeEach(function() {
        spyOn(this.view, 'renderAttrs');
        spyOn(this.view, 'markAsStaff');
        return spyOn(this.view, 'convertMath');
      });
      it('produces the correct HTML', function() {
        this.view.render();
        return expect(this.view.el.innerHTML).toContain('"discussion-flag-abuse notflagged"');
      });
      it('can be flagged for abuse', function() {
        this.response.flagAbuse();
        return expect(this.response.get('abuse_flaggers')).toEqual(['123', '567']);
      });
      return it('can be unflagged for abuse', function() {
        var temp_array;
        temp_array = [];
        temp_array.push(window.user.get('id'));
        this.response.set("abuse_flaggers", temp_array);
        this.response.unflagAbuse();
        return expect(this.response.get('abuse_flaggers')).toEqual([]);
      });
    });
  });

}).call(this);
