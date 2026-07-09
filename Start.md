# 
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no" />
    
    <!-- Basic Meta -->
    <title>Murdoku – Murder Mystery meets Sudoku</title>
    <meta name="description" content="Read the clues and use logic to place suspects on the crime scene. One person per row and per column, the victim is in the final square alone with the murderer. New weekly free puzzles. Free to play." />
    <meta name="keywords" content="murdoku, logic puzzle, murder mystery game, deduction puzzle, whodunit, brain teaser, puzzle game, free logic game, sudoku alternative, detective game, clue-based puzzle" />
    <meta name="author" content="Murdoku" />
    
    <!-- Theme & Display -->
    <meta name="theme-color" content="#0e0b13" />
    <meta name="color-scheme" content="light dark" />
    <meta name="darkreader-lock" />
    
    <!-- Favicon & Icons -->
    <!-- Explicit /play/ paths: the app is served under /play/ (Vite base='/play/',
         .htaccess RewriteBase /play/). A root-absolute "/favicon.png" wrongly hits
         the site root (the landing site), which is why /play had no icon while the
         root site did. Relative paths would break at "/play" without a trailing
         slash, so the explicit /play/ prefix is the robust choice. ?v=2 busts the
         1-year immutable image cache set in .htaccess. -->
    <link rel="icon" type="image/png" sizes="32x32" href="/play/favicon-32x32.png?v=2" />
    <link rel="icon" type="image/png" sizes="16x16" href="/play/favicon-16x16.png?v=2" />
    <link rel="icon" type="image/x-icon" href="/play/favicon.ico?v=2" />
    <link rel="apple-touch-icon" sizes="180x180" href="/play/apple-touch-icon.png?v=2" />
    <link rel="manifest" href="/play/site.webmanifest" />
    
    <!-- Open Graph (Facebook, LinkedIn, Discord, etc.) -->
    <meta property="og:type" content="website" />
    <meta property="og:title" content="Murdoku – Murder Mystery meets Sudoku" />
    <meta property="og:description" content="Read the clues and use logic to place suspects on the crime scene. One person per row and per column, the victim is in the final square alone with the murderer. New weekly free puzzles." />
    <meta property="og:image" content="https://murdoku.com/og-image.png" />
    <meta property="og:url" content="https://murdoku.com/play" />
    <meta property="og:site_name" content="Murdoku" />
    <meta property="og:locale" content="en_US" />
    
    <!-- Twitter Card -->
    <meta name="twitter:card" content="summary_large_image" />
    <meta name="twitter:title" content="Murdoku – Murder Mystery meets Sudoku" />
    <meta name="twitter:description" content="Read the clues and use logic to place suspects on the crime scene. One person per row and per column, the victim is in the final square alone with the murderer." />
    <meta name="twitter:image" content="https://murdoku.com/og-image.png" />
    
    <!-- Mobile App Meta -->
    <meta name="mobile-web-app-capable" content="yes" />
    <meta name="apple-mobile-web-app-capable" content="yes" />
    <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent" />
    <meta name="apple-mobile-web-app-title" content="Murdoku" />
    
    <!-- SEO -->
    <link rel="canonical" href="https://murdoku.com/play" />
    <meta name="robots" content="index, follow" />
    
    <!-- Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Caveat:wght@500;700&family=Inter:wght@400;600;800&display=swap" rel="stylesheet">
    <!-- Adobe Fonts: Add your Typekit kit with "Relation" here, then you can remove Caveat above -->
    <!-- <link rel="stylesheet" href="https://use.typekit.net/YOUR_KIT_ID.css"> -->
    <script type="module" crossorigin src="/play/assets/index-cYM4feTt.js"></script>
    <link rel="modulepreload" crossorigin href="/play/assets/react-vendor-wrsPLQQ4.js">
    <link rel="modulepreload" crossorigin href="/play/assets/firebase-core-N4pxKsV9.js">
    <link rel="modulepreload" crossorigin href="/play/assets/firebase-firestore-CVtK1c4k.js">
    <link rel="modulepreload" crossorigin href="/play/assets/app-core-LYtmN_Uz.js">
    <link rel="modulepreload" crossorigin href="/play/assets/lang-data-DIr4higw.js">
    <link rel="modulepreload" crossorigin href="/play/assets/puzzle-core-6eVPDJ_g.js">
    <link rel="modulepreload" crossorigin href="/play/assets/debug-DzkGgEFP.js">
    <link rel="modulepreload" crossorigin href="/play/assets/generator-DX666n53.js">
    <link rel="stylesheet" crossorigin href="/play/assets/index-By7Q7oUV.css">
  </head>
  <body class="loading">
    <div id="root"></div>
    <script>
      // Remove loading class when browser is idle (or after 1.5s max)
      // This re-enables animations after initial render is complete
      var done = false;
      var removeLoading = function() {
        if (done) return;
        done = true;
        document.body.classList.remove('loading');
      };
      if ('requestIdleCallback' in window) {
        requestIdleCallback(removeLoading, { timeout: 1500 });
      } else {
        setTimeout(removeLoading, 1500);
      }
      // Also enable on first interaction (including hover)
      document.addEventListener('click', removeLoading, { once: true });
      document.addEventListener('touchstart', removeLoading, { once: true });
      document.addEventListener('mouseover', removeLoading, { once: true });
    </script>
  </body>
</html>
