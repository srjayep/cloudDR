    $(document).ready(function() {
        $('#sample_1').dataTable( {
            "bAutoWidth": true,
            "bSort": false,
            "bProcessing": true,
            "ajax": "../disasterdrilldata/",
            "columns": [
                { "data": "appGroup" },
                { "data": "clientName" },
                { "data": "type" },
                { "data": "state" },

            ],

            "columnDefs": [{
                    "targets": 0,
                    "mRender":function(data,type,full){
                        return "<a id='editapp'  data-toggle='modal'  data-target='#static1'>" + data+"</a>"
                    }
            }],
            "oLanguage": {
            "sLengthMenu": "&nbsp;&nbsp;每页显示 _MENU_ 条记录",
            "sZeroRecords": "抱歉， 没有找到",
            "sInfo": "从 _START_ 到 _END_ /共 _TOTAL_ 条数据",
            "sInfoEmpty":'',
            "sInfoFiltered": "(从 _MAX_ 条数据中检索)",
            "sSearch": "搜索",
            "oPaginate": {
            "sFirst": "首页",
            "sPrevious": "前一页",
            "sNext": "后一页",
            "sLast": "尾页"
            },
            "sZeroRecords": "没有检索到数据",

            }
            } );
        // 行按钮

        $('#sample_1 tbody').on( 'click', 'a#editapp', function () {
                var table = $('#sample_1').DataTable();
                var data = table.row( $(this).parents('tr') ).data();
                $("#dataSetGUID").val(data.dataSetGUID);
                $("#clientGUID").val(data.clientGUID);
                $("#appGroup").val(data.appGroup);
                $("#type").val(data.type);
                $("#vmlist").empty();
                $("#vmdiv").hide();
                $("#resourcepool").empty();
                $("#computerresource").empty();
                if (data.type=="VMWARE"){
                    $("#vmdiv").show();
                    for (var i=0;i<data.backupContent.length;i++){

                            $("#vmlist").append("<option value='" + data.backupContent[i] + "'>" + data.backupContent[i] + "</option>");
                    }
                    $.ajax({
                        type: "POST",
                        url: "../vmresourcepooldatafordrill/",
                        success:function(data){
                                var dataObj=eval("("+data+")");
                                for (var i=0;i<dataObj.data.length;i++){
                                    if (i==0)
                                    {
                                        $("#resourcepool").append("<option selected value='" + dataObj.data[i].id + "'>" + dataObj.data[i].name + "</option>");
                                         for (var j=0;j<(dataObj.data[i].myresource).length;j++){
                                            $("#computerresource").append("<option selected value='" + dataObj.data[i].myresource[j].id + "'>" + dataObj.data[i].myresource[j].name + "</option>");

                                        }
                                    }
                                    else
                                        $("#resourcepool").append("<option  value='" + dataObj.data[i].id + "'>" + dataObj.data[i].name + "</option>");

                            }
                        },
                    });
                }
                else
                {
                    $.ajax({
                        type: "POST",
                        url: "../computerresourcepooldatafordrill/",
                        success:function(data){
                                var dataObj=eval("("+data+")");
                                for (var i=0;i<dataObj.data.length;i++){
                                    if (i==0)
                                    {
                                        $("#resourcepool").append("<option selected value='" + dataObj.data[i].id + "'>" + dataObj.data[i].name + "</option>");
                                         for (var j=0;j<(dataObj.data[i].myresource).length;j++){
                                            $("#computerresource").append("<option selected value='" + dataObj.data[i].myresource[j].id + "'>" + dataObj.data[i].myresource[j].name + "</option>");

                                        }
                                    }
                                    else
                                        $("#resourcepool").append("<option  value='" + dataObj.data[i].id + "'>" + dataObj.data[i].name + "</option>");
                            }
                        },
                    });
                }
        });

        $("#resourcepool").change(function(){
             $("#computerresource").empty();
              $("#computerresource").val("")
              $("#computerresource").text("")
            if($("#type").val()=="VMWARE"){

                $.ajax({
                    type: "POST",
                    url: "../vmresourcedatafordrill/",
                    data:
                        {
                          id:$("#resourcepool").val()
                        },
                    success:function(data){
                            var dataObj=eval("("+data+")");
                            for (var i=0;i<dataObj.data.length;i++){
                                    $("#computerresource").append("<option selected value='" + dataObj.data[i].id + "'>" + dataObj.data[i].name + "</option>");

                        }
                    },
                });
            }
            else{
                $.ajax({
                    type: "POST",
                    url: "../computerresourcedatafordrill/",
                    data:
                        {
                          id:$("#resourcepool").val()
                        },
                    success:function(data){
                            var dataObj=eval("("+data+")");
                            for (var i=0;i<dataObj.data.length;i++){
                                    $("#computerresource").append("<option selected value='" + dataObj.data[i].id + "'>" + dataObj.data[i].name + "</option>");
                        }
                    },
                });

            }
        });

         $('#next1').click(function(){
            $("#li2").tab("show");
        })
        $('#next2').click(function(){
            $("#li3").tab("show");
        })
        $('#next3').click(function(){
            $("#li4").tab("show");
        })
        $('#last2').click(function(){
            $("#li1").tab("show");
        })
        $('#last3').click(function(){
            $("#li2").tab("show");
        })
        $('#last4').click(function(){
            $("#li3").tab("show");
        })
        $('#next4').click(function(){

        })

    } );