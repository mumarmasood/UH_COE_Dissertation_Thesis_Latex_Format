\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{uhcoethesis}[2026/05/29 University of Houston thesis class]

\LoadClass[12pt,oneside,openany]{report}

\RequirePackage[letterpaper,left=1.5in,right=1in,top=1in,bottom=1in,footskip=0.5in]{geometry}
\RequirePackage{setspace}
\RequirePackage{indentfirst}
% The LaTeX tagging layer used for accessible PDF/UA output owns the
% sectioning, float-caption, and table-of-contents commands.  caption,
% titlesec, and tocloft predate those interfaces and replace the tagged
% commands.  Keep them for older, untagged installations, and use equivalent
% visual formatting that leaves the tagged commands intact in current builds.
\IfFormatAtLeastTF{2025-11-01}{}{%
  \RequirePackage{caption}%
  \RequirePackage{titlesec}%
  \RequirePackage{tocloft}%
}
\RequirePackage{etoolbox}
\RequirePackage{amsmath}
% LuaMML works most reliably with Unicode math fonts.  Traditional TeX math
% fonts emit non-Unicode accent bytes (for example in \ddot), which make the
% generated MathML auxiliary file fail on the next tagged compilation.
\IfFormatAtLeastTF{2025-11-01}{%
  \ifluatex\RequirePackage{unicode-math}\fi
}{}
\RequirePackage{graphicx}
\RequirePackage[hidelinks,hypertexnames=false]{hyperref}

\doublespacing
\IfFormatAtLeastTF{2025-11-01}{}{%
  \captionsetup{font={normalsize,stretch=1},format=hang,justification=raggedright,singlelinecheck=false}%
}

\pagestyle{plain}
\pagenumbering{roman}

\setlength{\parindent}{0.5in}
\setlength{\parskip}{0pt}
% Give TeX a small amount of last-resort flexibility for long technical
% compounds and bibliography URLs instead of allowing text into the margin.
\setlength{\emergencystretch}{3em}

\makeatletter
\IfFormatAtLeastTF{2025-11-01}{%
  % Match the former tocloft layout without replacing the tagging-aware
  % \@starttoc implementation.
  \renewcommand*\l@chapter[2]{%
    \@dottedtocline{0}{0pt}{1.5em}{\bfseries #1}{\bfseries #2}%
  }
  \renewcommand*\l@section{\@dottedtocline{1}{1.5em}{2.3em}}
  \renewcommand*\l@subsection{\@dottedtocline{2}{3.5em}{3.2em}}
  \renewcommand*\l@figure{\@dottedtocline{1}{1.5em}{4em}}
  \let\l@table\l@figure
  \renewcommand{\@pnumwidth}{2em}%
  % Keep the tagging layer's caption structure and modify only its paragraph
  % shape so continuation lines align with the start of the caption text.
  \AddToHookWithArguments{cmd/@makecaption/before}{%
    \setstretch{1}\normalsize
    \sbox\@tempboxa{#1:\space}%
    \hangindent=\wd\@tempboxa
    \hangafter=1
  }%
}{%
  \setlength{\cftbeforechapskip}{0pt}%
  \setlength{\cftbeforesecskip}{0pt}%
  \setlength{\cftchapindent}{0pt}%
  \setlength{\cftsecindent}{1.5em}%
  \setlength{\cftsubsecindent}{3.5em}%
}

\widowpenalty=10000
\clubpenalty=10000
\displaywidowpenalty=10000
\brokenpenalty=10000

\renewcommand{\contentsname}{TABLE OF CONTENTS}
\renewcommand{\listtablename}{LIST OF TABLES}
\renewcommand{\listfigurename}{LIST OF FIGURES}
\renewcommand{\bibname}{REFERENCES}
\renewcommand{\chaptername}{Chapter}
\renewcommand{\thechapter}{\arabic{chapter}}
\numberwithin{equation}{chapter}

\IfFormatAtLeastTF{2025-11-01}{%
  % Customize only the visual chapter heads.  The tagging-aware \chapter
  % command itself remains untouched.
  \renewcommand{\@makechapterhead}[1]{%
    \vspace*{-50pt}%
    {\parindent\z@\raggedright\normalfont
      \huge\bfseries \chaptername\ \thechapter\par
      \nobreak\vskip0.75\baselineskip
      \interlinepenalty\@M
      \huge\bfseries #1\par
      \nobreak\vskip1.5\baselineskip
    }%
  }
  \renewcommand{\@makeschapterhead}[1]{%
    \vspace*{-50pt}%
    {\parindent\z@\centering\normalfont
      \interlinepenalty\@M
      \MakeUppercase{#1}\par
      \nobreak\vskip1.5\baselineskip
    }%
  }
}{%
  \setlength{\cftfignumwidth}{4em}%
  \setlength{\cfttabnumwidth}{4em}%
  \setlength{\cftbeforefigskip}{0pt}%

  \titleformat{name=\chapter}[display]
    {\normalfont\huge\bfseries}
    {\chaptername\ \thechapter}
    {0.75\baselineskip}
    {}

  \titleformat{name=\chapter,numberless}[display]
    {\normalfont\centering}
    {}
    {0pt}
    {\MakeUppercase}

  \titlespacing*{\chapter}{0pt}{-50pt}{1.5\baselineskip}%
}

\makeatletter
\def\ps@plain{%
  \let\@mkboth\@gobbletwo
  \let\@oddhead\@empty
  \def\@oddfoot{\reset@font\hfil\thepage\hfil}
  \let\@evenhead\@empty
  \let\@evenfoot\@oddfoot
}

\newcommand{\@department}{}
\newcommand{\@college}{Cullen College of Engineering}
\newcommand{\@degree}{}
\newcommand{\@major}{}
\newcommand{\@degreemonth}{}
\newcommand{\@degreeyear}{}
\newcommand{\@chair}{}
\newcommand{\@cochair}{}
\newcommand{\@committeelist}{}
\newcommand{\@committeehonorific}{}
\newcommand{\@submissiontype}{dissertation}

\newcommand{\department}[1]{\gdef\@department{#1}}
\newcommand{\college}[1]{\gdef\@college{#1}}
\newcommand{\degree}[1]{\gdef\@degree{#1}}
\newcommand{\major}[1]{\gdef\@major{#1}}
\newcommand{\degreemonth}[1]{\gdef\@degreemonth{#1}}
\newcommand{\degreeyear}[1]{\gdef\@degreeyear{#1}}
\newcommand{\chair}[1]{\gdef\@chair{#1}}
\newcommand{\cochair}[1]{\gdef\@cochair{#1}}
\newcommand{\committeehonorific}[1]{\gdef\@committeehonorific{#1}}
\newcommand{\submissiontype}[1]{\gdef\@submissiontype{#1}}
\newcommand{\@committeename}[1]{%
  \ifdefempty{\@committeehonorific}{#1}{\@committeehonorific\ #1}%
}
\newcommand{\committeemember}[1]{%
  \gappto\@committeelist{Committee Member: & \@committeename{#1}\\[0.10\baselineskip]}%
}

\newcommand{\frontmatter}{%
  \clearpage
  \pagenumbering{roman}%
  \setcounter{page}{1}%
}

\newcommand{\mainmatter}{%
  \clearpage
  \pagenumbering{arabic}%
  \setcounter{page}{1}%
}

\newcommand{\backmatter}{\clearpage}

\newcommand{\maketitlepage}{%
  \begin{titlepage}
    \thispagestyle{empty}
    \begingroup
    \doublespacing
    \begin{center}
      \vspace*{0.25in}
      {\Large
      \begin{minipage}{0.82\textwidth}
        \centering
        \@title
      \end{minipage}\par}
      \vspace{0.35in}
      by\par
      \@author\par
      \vspace{0.60in}
      A \@submissiontype\ submitted to the \\ \@department,\par
      \vspace{0.10\baselineskip}
      \@college\par
      \vspace{0.10\baselineskip}
      in partial fulfillment of the requirements for the degree of\par
      \vspace{0.55\baselineskip}
      \@degree\par
      in \@major\par
      \vspace{0.45in}
      \begin{tabular}{@{}r@{\ }l@{}}
        Chair of Committee: & \@committeename{\@chair}\\[0.10\baselineskip]
        \ifdefempty{\@cochair}{}{Co-Chair of Committee: & \@committeename{\@cochair}\\[0.10\baselineskip]}
        \@committeelist
      \end{tabular}\par
      \vfill
      University of Houston\par
      \@degreemonth\ \@degreeyear\par
      \vspace*{0.25in}
    \end{center}
    \endgroup
  \end{titlepage}
  % The title page is Roman page i, although its number is not printed.
  % The titlepage environment resets the counter, so advance it explicitly.
  \setcounter{page}{2}%
}

\newcommand{\makecopyrightpage}{%
  \clearpage
  \thispagestyle{empty}
  \null
  \vfill
  \begin{center}
    Copyright \@degreeyear, \@author
  \end{center}
  \vfill
  \clearpage
}

\newenvironment{dedication}{%
  \chapter*{DEDICATION/EPIGRAPH}
  \addcontentsline{toc}{chapter}{DEDICATION/EPIGRAPH}
}{\clearpage}

\newenvironment{acknowledgements}{%
  \chapter*{ACKNOWLEDGEMENTS}
  \addcontentsline{toc}{chapter}{ACKNOWLEDGEMENTS}
}{\clearpage}

\newenvironment{abstractpage}{%
  \chapter*{ABSTRACT}
  \addcontentsline{toc}{chapter}{ABSTRACT}
}{\clearpage}

\newenvironment{nomenclaturepage}{%
  \chapter*{NOMENCLATURE}
  \addcontentsline{toc}{chapter}{NOMENCLATURE}
}{\clearpage}

% Apply these patches after tocloft installs its final list commands.
\AtBeginDocument{%
  \pretocmd{\tableofcontents}{\clearpage}{}{}%
  \pretocmd{\listoftables}{%
    \clearpage
    \phantomsection
    \addcontentsline{toc}{chapter}{\listtablename}%
  }{}{}%
  \pretocmd{\listoffigures}{%
    \clearpage
    \phantomsection
    \addcontentsline{toc}{chapter}{\listfigurename}%
    \begingroup\setstretch{1}%
  }{}{}%
  \apptocmd{\tableofcontents}{\clearpage}{}{}%
  \apptocmd{\listoftables}{\clearpage}{}{}%
  \apptocmd{\listoffigures}{\endgroup\clearpage}{}{}%
}
\makeatother
