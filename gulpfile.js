var gulp = require('gulp');
var connect = require('gulp-connect');
var bowerFiles = require('gulp-main-bower-files');
var inject = require('gulp-inject');
var debug = require('gulp-debug');
var filter = require('gulp-filter');
var less = require('gulp-less');
var sourcemaps = require('gulp-sourcemaps');
var angularFilesort = require('gulp-angular-filesort');
var clean = require('gulp-clean');


var outputDev = {
    allJs: './app/static/js',
    jsVendors: './app/static/js/vendors',
    css: './app/static/styles'

}

var src = {
    less: ['./less/*.less'],
    coffee: ['assets/**/*.coffee'],
    js: ['src/js/**/*.js'],
    bower: ['bower.json', '.bowerrc']
}

var filterByExtension = function (extension) {
    return filter(function (file) {
        return file.path.match(new RegExp('.' + extension + '$'));
    });
};

gulp.task('clean', function () {
    //return gulp.src(outputDev.allJs + '/*', {
    //        read: false
    //    })
    //    .pipe(clean());
});

gulp.task('bowerJs', ['clean'], function () {
    var jsFilter = filterByExtension('js');
    return gulp.src(src.bower[0])
        .pipe(bowerFiles())
        .pipe(jsFilter)
        .pipe(gulp.dest(outputDev.jsVendors));
});

gulp.task('myJs', ['clean'], function () {
    //return gulp.src(src.js)
    //.pipe(gulp.dest(outputDev.myJs));
});

gulp.task('buildCss', ['clean'], function () {
    gulp.src(src.less)
        .pipe(sourcemaps.init())
        .pipe(less())
        .pipe(sourcemaps.write())
        .pipe(gulp.dest(outputDev.css))
});

gulp.task('inject', ['bowerJs', 'buildCss'], function () {
    gulp.src('./app/tempalte/base.html')
        //.pipe(debug({title: 'unicorn:'}))
        .pipe(inject(gulp.src(outputDev.jsVendors + '/**/*.js'), {
            name: 'vendors'
        }))
        .pipe(inject(gulp.src('./app/js/*.js').pipe(angularFilesort())))
        .pipe(inject(gulp.src('./app/styles/**/*.css')))
        .pipe(gulp.dest('./app'))
        .pipe(connect.reload());
});

gulp.task('connect', ['inject'], function () {
    connect.server({
        root: ['./'],
        livereload: true
    });
});


gulp.task('watch', ['connect'], function () {
    gulp.watch(['./bower.json', './.bowerrc'], ['bowerJs']);
    gulp.watch('./src/js/**/*.js', ['myJs', 'inject']);
    gulp.watch('./less/**/*.less', ['buildCss']);

});

gulp.task('default', ['clean', 'bowerJs', 'buildCss', 'inject', 'connect', 'watch']);
