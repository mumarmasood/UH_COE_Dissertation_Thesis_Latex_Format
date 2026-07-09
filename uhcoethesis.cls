\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{uhcoethesis}[2026/05/29 University of Houston thesis class]

\LoadClass[12pt,oneside,openany]{report}

\RequirePackage[letterpaper,left=1.5in,right=1in,top=1in,bottom=1in,footskip=0.5in]{geometry}
\RequirePackage{setspace}
\RequirePackage{caption}
\RequirePackage{titlesec}
\RequirePackage{tocloft}
\RequirePackage{etoolbox}
\RequirePackage{amsmath}
\RequirePackage{graphicx}
\RequirePackage[hidelinks,hypertexnames=false]{hyperref}

\doublespacing
\captionsetup{font={normalsize,stretch=1},justification=raggedright,singlelinecheck=false}

\pagestyle{plain}
\pagenumbering{roman}

\setlength{\parindent}{0.5in}
\setlength{\parskip}{0pt}
\setlength{\cftbeforechapskip}{0pt}
\setlength{\cftbeforesecskip}{0pt}
\setlength{\cftchapindent}{0pt}
\setlength{\cftsecindent}{1.5em}
\setlength{\cftsubsecindent}{3.5em}

\widowpenalty=10000
\clubpenalty=10000
\displaywidowpenalty=10000
\brokenpenalty=10000

\renewcommand{\contentsname}{TABLE OF CONTENTS}
\renewcommand{\listtablename}{LIST OF TABLES}
\renewcommand{\listfigurename}{LIST OF FIGURES}
\renewcommand{\bibname}{REFERENCES}
\renewcommand{\chaptername}{CHAPTER}
\renewcommand{\thechapter}{\Roman{chapter}}
\numberwithin{equation}{chapter}

\titleformat{name=\chapter}[display]
  {\normalfont\centering}
  {\MakeUppercase{\chaptername\ \thechapter}}
  {0.75\baselineskip}
  {\MakeUppercase}

\titleformat{name=\chapter,numberless}[display]
  {\normalfont\centering}
  {}
  {0pt}
  {\MakeUppercase}

\titlespacing*{\chapter}{0pt}{0pt}{1.5\baselineskip}

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
\newcommand{\@degreedate}{}
\newcommand{\@chair}{}
\newcommand{\@cochair}{}
\newcommand{\@committeelist}{}
\newcommand{\@committeehonorific}{Dr.}
\newcommand{\@submissiontype}{dissertation}

\newcommand{\department}[1]{\gdef\@department{#1}}
\newcommand{\college}[1]{\gdef\@college{#1}}
\newcommand{\degree}[1]{\gdef\@degree{#1}}
\newcommand{\major}[1]{\gdef\@major{#1}}
\newcommand{\degreedate}[1]{\gdef\@degreedate{#1}}
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
      A \@submissiontype\ submitted to the \@department,\par
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
      \@degreedate\par
      \vspace*{0.25in}
    \end{center}
    \endgroup
  \end{titlepage}
}

\newcommand{\makecopyrightpage}{%
  \clearpage
  \thispagestyle{empty}
  \null
  \vfill
  \begin{center}
    Copyright \@degreedate, \@author
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

\pretocmd{\tableofcontents}{\clearpage}{}{}
\pretocmd{\listoftables}{\clearpage}{}{}
\pretocmd{\listoffigures}{\clearpage}{}{}
\apptocmd{\tableofcontents}{\clearpage}{}{}
\apptocmd{\listoftables}{\clearpage}{}{}
\apptocmd{\listoffigures}{\clearpage}{}{}
\makeatother
