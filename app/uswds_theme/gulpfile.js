const uswds = require("@uswds/compile");
const {parallel, watch, series, src} = require('gulp');
const gulp = require("gulp");
const browsersync = require('browser-sync').create();
const uglifyes = require('uglify-es');
const composer = require('gulp-uglify/composer');
const uglify = composer(uglifyes, console);

const settings = {
  sass: {
    src: ['./src/sass/**/*.scss']
  },
  js: {
    dest: './static/js',
    minDest: './static/js/min',
    minSrc: './src/js/**/*.js',
    src: './src/js/**/*.js'
  }
}

// JS build function.
function buildJS() {
  return src(settings.js.src)
    .pipe(uglify())
    .pipe(gulp.dest(settings.js.dest))
}

// Watch changes on JS and twig files and trigger functions at the end.
function watchJSTwigFiles() {
  watch(
    [
      './src/js/**/*.js',
      './templates/**/*.html'
    ],
    {
      events: 'all',
      ignoreInitial: false
    },
    series(
      buildJS,
      browserSyncReload
    )
  );
}

// BrowserSync Reload
function browserSyncReload(done) {
  browsersync.reload();
  done();
}

// Compile CSS from scss.
function buildCompStyles() {
  return src(settings.sass.src)
    .pipe(browsersync.reload({
      stream: true
    }));
}

// Watch changes on sass files and trigger functions at the end.
function watchCompFiles() {
  watch(
    [
      './src/sass/**/*.scss',
    ],
    {
      events: 'all',
      ignoreInitial: false
    },
    series(
      buildCompStyles
    )
  );
}

// Init BrowserSync.
function browserSync(done) {
  browsersync.init({
    injectChanges: true,
    logPrefix: 'OneUSDA Theme (USWDS)',
    baseDir: './',
    open: false,
    notify: true,
    proxy: 'd94.lndo.site',
    host: 'd94.lndo.site',
    openBrowserAtStart: false,
    reloadOnRestart: true,
    port: 32654,
    ui: false,
  });
  done();
}

/**
 * USWDS version
 */
// Use version 3.
uswds.settings.version = 3;

/**
 * Custom path settings
 * Set as many as you need
 * see https://designsystem.digital.gov/documentation/getting-started/developers/phase-two-compile/#step-4-create-path-settings-and-export-compile-functions
 */
uswds.paths.dist.theme = './src/sass';
uswds.paths.dist.css = './static/css';
uswds.paths.dist.img = './static/img';
uswds.paths.dist.fonts = './static/fonts';
uswds.paths.dist.js = './static/js';
uswds.paths.src.projectSass = './src/sass';

/**
 * Exports
 * Add as many as you need
 */

// Init project
// init commented out as it is only used once at the very beginning of the project.
// exports.init = uswds.init;

// Various compile functions.
exports.compile = uswds.compile;
exports.watch = parallel(watchCompFiles, uswds.watch, browserSync, watchJSTwigFiles);
exports.update = uswds.updateUswds;
exports.default = uswds.watch;
exports.copyAssets = uswds.copyAssets;
