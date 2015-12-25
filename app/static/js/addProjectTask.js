$("#data-table-task").bootgrid({
    ajax: false,
    requestHandler: function (request)
    {
        console.log(request)
        /* To accumulate custom parameter with the request object */
        return {
            id: "b0df282a-0d67-40e5-8558-c9e93b7befed"
        };
    },
    formatters: {
        "commands": function(column, row) {
            return "<button type=\"button\" onclick=\"location.href='./add_project?projectName=" + row.id+"'\" class=\"btn btn-icon command-edit\" data-row-id=\"" + row.id + "\"><span class=\"zmdi zmdi-edit\"></span></button> " + 
            "<button type=\"button\" class=\"btn btn-icon command-delete\" onclik=\"location.href='./add_project?projectName=" + row.id+"' \"><span class=\"zmdi zmdi-delete\"></span></button>";
        }
    },
    //Selection
    css: {
        icon: 'zmdi icon',
        iconColumns: 'zmdi-view-module',
        iconDown: 'zmdi-expand-more',
        iconRefresh: 'zmdi-refresh',
        iconUp: 'zmdi-expand-less'
    },
    selection: true,
    multiSelect: false,
    rowSelect: flase,
    keepSelection: true
    
});