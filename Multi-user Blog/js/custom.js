/**
 * Created by Mohnish on 1/4/17.
 */

$('#footer').css('margin-top',
  $(document).height()
  - ( $('#header').height() + $('#content').height() )
  - $('#footer').height()
);