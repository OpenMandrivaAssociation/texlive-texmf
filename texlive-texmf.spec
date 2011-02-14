%define	__spec_install_pre	export RPM_SOURCE_DIR="%{_sourcedir}";export RPM_BUILD_DIR="%{_builddir}";export RPM_OPT_FLAGS="%{optflags}";export RPM_ARCH="%{_arch}";export RPM_OS="%{_os}";export RPM_DOC_DIR="%%{_docdir}";export RPM_PACKAGE_NAME="%%{name}";export RPM_PACKAGE_VERSION="%%{version}";export RPM_PACKAGE_RELEASE="%%{release}";export RPM_BUILD_ROOT="%{buildroot}";export LC_ALL=C;export LANG=C;cd %_builddir
%define enable_asymptote	0
%define enable_xindy		0

%define with_system_dialog	1
%define with_system_lcdf	0
%define with_system_poppler	0
%define with_system_psutils	1
%define with_system_t1lib	1
%define with_system_tex4ht	0

Name:		texlive-texmf
Version:	20100722
Release:	%mkrel 1
Summary:	The TeX formatting system
Group:		Publishing
License:	Apache2 and Artistic and BSD and FDL and Freeware and GFL and GFSL and GPL and GPLv2 and GPLv3 and LGPL and LGPLv2.1 and LPPL and LPPLv1 and LPPLv1.2 and LPPLv1.3 and OFL and Public Domain
URL:		http://tug.org/texlive/
Source0:	ftp://tug.org/historic/systems/texlive/2010/texlive-20100722-texmf.tar.xz
Source1:	ftp://tug.org/historic/systems/texlive/2010/texlive-20100722-texmf.tar.xz.sha256
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch

#-----------------------------------------------------------------------
Requires:	perl-Algorithm-Diff
Requires:	xdg-utils

Provides:	texlive-texmf-afm = %{version}
Obsoletes:	texlive-texmf-afm <= 2007
Provides:	texlive-texmf-cmsuper = %{version}
Obsoletes:	texlive-texmf-cmsuper <= 2007
Provides:	texlive-texmf-common = %{version}
Obsoletes:	texlive-texmf-common <= 2007
Provides:	texlive-texmf-context = %{version}
Obsoletes:	texlive-texmf-context <= 2007
Provides:	texlive-texmf-dvipdfm = %{version}
Obsoletes:	texlive-texmf-dvipdfm <= 2007
Provides:	texlive-texmf-dvips = %{version}
Obsoletes:	texlive-texmf-dvips <= 2007

%if %mdkversion <= 201100
Provides:	texlive-texmf-jadetex = %{version}
Obsoletes:	texlive-texmf-jadetex <= 2007
%endif

Provides:	texlive-texmf-latex = %{version}
Obsoletes:	texlive-texmf-latex <= 2007

%if %mdkversion <= 201100
Provides:	texlive-texmf-usrlocal = %{version}
Obsoletes:	texlive-texmf-usrlocal <= 2007
%endif

Provides:	texlive-texmf-xmltex = %{version}
Obsoletes:	texlive-texmf-xmltex <= 2007

Provides:	texmf-data = %{version}

#-----------------------------------------------------------------------
Patch0:		texlive-20100722-texmf-default.patch

#-----------------------------------------------------------------------
%description
TeX Live is an easy way to get up and running with the TeX document
production system. It provides a comprehensive TeX system. It includes
all the major TeX-related programs, macro packages, and fonts that are
free software, including support for many languages around the world.

%files
%defattr(-,root,root,-)
%{_bindir}/*
%{_datadir}/X11/app-defaults/XDvi
%{_datadir}/texmf/chktex
%{_datadir}/texmf/scripts
%{_datadir}/texmf/texconfig
%{_datadir}/texmf/web2c
%{_datadir}/texmf/xdvi
%{_datadir}/texmf-dist/bibtex
%{_datadir}/texmf-dist/context
%{_datadir}/texmf-dist/dvips
%{_datadir}/texmf-dist/makeindex
%{_datadir}/texmf-dist/metafont
%{_datadir}/texmf-dist/metapost
%{_datadir}/texmf-dist/mft
%{_datadir}/texmf-dist/omega
%{_datadir}/texmf-dist/pbibtex
%{_datadir}/texmf-dist/scripts
%{_datadir}/texmf-dist/source
%{_datadir}/texmf-dist/tex
%{_datadir}/texmf-dist/tex4ht
%{_datadir}/texmf-dist/vtex

#-----------------------------------------------------------------------
%package	-n texlive-doc
Summary:	Tex Live documentation
Group:		Publishing

%description	-n texlive-doc
TeX Live is an easy way to get up and running with the TeX document
production system. It provides a comprehensive TeX system. It includes
all the major TeX-related programs, macro packages, and fonts that are
free software, including support for many languages around the world.

%files		-n texlive-doc
%defattr(-,root,root,-)
%{_datadir}/texmf/doc
%{_datadir}/texmf-dist/doc

#-----------------------------------------------------------------------
%package	-n texlive-fonts
Summary:	Tex Live fonts
Group:		Publishing

%description	-n texlive-fonts
TeX Live is an easy way to get up and running with the TeX document
production system. It provides a comprehensive TeX system. It includes
all the major TeX-related programs, macro packages, and fonts that are
free software, including support for many languages around the world.

%files		-n texlive-fonts
%defattr(-,root,root,-)
%{_datadir}/fonts/texmf
%{_datadir}/fonts/texmf-dist
%{_datadir}/texmf/fonts
%{_datadir}/texmf-dist/fonts

#-----------------------------------------------------------------------
%prep
%setup -q -n texlive-20100722-texmf

perl -pi -e 's%^(TEXMFMAIN\s+= ).*%$1%{_datadir}/texmf%;'				\
	 -e 's%^(TEXMFDIST\s+= ).*%$1%{_datadir}/texmf-dist%;'				\
	 -e 's%^(TEXMFLOCAL\s+= ).*%$1\{%{_datadir}/texmf-local,%{_datadir}/texmf\}%;'	\
	 -e 's%^(TEXMFSYSVAR\s+= ).*%$1%{_localstatedir}/lib/texmf%;'			\
	 -e 's%^(TEXMFSYSCONFIG\s+= ).*%$1%{_datadir}/texmf-config%;'			\
	 -e 's%^(TEXMFHOME\s+= ).*%$1\{\$HOME/texmf,%{_datadir}/texmf\}%;'		\
	 -e 's%^(TEXMFVAR\s+= ).*%$1\$HOME/.texlive2010/texmf-var%;'			\
	 -e 's%^(TEXMFCONFIG\s+= ).*%$1\$HOME/.texlive2010/texmf-config%;'		\
	 -e 's%^(OSFONTDIR\s+= ).*%$1%{_datadir}/fonts%;'				\
	texmf/web2c/texmf.cnf

perl -pi -e 's%^(TEXMFMAIN\s+= ).*%$1%{_datadir}/texmf%;'					 \
	 -e 's%^(TEXMFLOCAL\s+= ).*%$1\{%{_datadir}/texmf-local,%{_datadir}/texmf\}%;'		 \
	 -e 's%^(TEXMFFONTS\s+= ).*%$1\{%{_datadir}/texmf/fonts,%{_datadir}/texmf-dist/fonts\}%;'\
	 -e 's%^(TEXMFEXTRA\s+= ).*%$1\{%{_datadir}/texmf-extra,%{_datadir}/texmf\}%;'		 \
	 -e 's%^(TEXMFPROJECT\s+= ).*%$1\{%{_datadir}/texmf-project,%{_datadir}/texmf\}%;'	 \
	 -e 's%^(VARTEXMF\s+= ).*%$1\$HOME/.texlive2010/texmf-var%;'				 \
	 -e 's%^(HOMETEXMF\s+= ).*%$1\{\$HOME/texmf,%{_datadir}/texmf\}%;'			 \
	 -e 's%^(TEXMFCNF\s+= ).*%$1%{_datadir}/texmf/web2c%;'					 \
	texmf/web2c/context.cnf

perl -pi -e 's%^(TEXMFCACHE\s+= ).*%$1\$HOME/.texlive2010/texmf-var%;'	\
	texmf/web2c/texmfcnf.lua

perl -pi -e 's%^# (viewer_pdf = )xpdf.*%$1xdg-open%;'	\
	texmf/texdoc/texdoc.cnf

%patch0 -p1

#-----------------------------------------------------------------------
%build
mkdir -p %{buildroot}%{_datadir}
cp -far * %{buildroot}%{_datadir}

#-----------------------------------------------------------------------
%install

mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
    ln -sf a2ping	../share/texmf/scripts/a2ping/a2ping.pl
    ln -sf afm2afm	../share/texmf-dist/scripts/fontools/afm2afm
    ln -sf arlatex	../share/texmf-dist/scripts/bundledoc/arlatex
    ln -sf authorindex	../share/texmf-dist/scripts/authorindex/authorindex
    ln -sf autoinst	../share/texmf-dist/scripts/fontools/autoinst
    ln -sf bibexport	../share/texmf-dist/scripts/bibexport/bibexport.sh
    ln -sf bundledoc	../share/texmf-dist/scripts/bundledoc/bundledoc
    ln -sf cachepic	../share/texmf-dist/scripts/cachepic/cachepic.tlu
    ln -sf cmap2enc	../share/texmf-dist/scripts/fontools/cmap2enc
    ln -sf de-macro	../share/texmf-dist/scripts/de-macro/de-macro
    ln -sf dviasm	../share/texmf-dist/scripts/dviasm/dviasm.py
    ln -sf e2pall	../share/texmf/scripts/tetex/e2pall.pl
    ln -sf ebong	../share/texmf-dist/scripts/bengali/ebong.py
    ln -sf epspdf	../share/texmf-dist/scripts/epspdf/epspdf
    ln -sf epspdftk	../share/texmf-dist/scripts/epspdf/epspdftk
    ln -sf epstopdf	../share/texmf-dist/scripts/epstopdf/epstopdf.pl
    ln -sf fig4latex	../share/texmf-dist/scripts/fig4latex/fig4latex
    ln -sf findhyph	../share/texmf-dist/scripts/findhyph/findhyph
    ln -sf font2afm	../share/texmf-dist/scripts/fontools/font2afm
    ln -sf fragmaster	../share/texmf-dist/scripts/fragmaster/fragmaster.pl
%if !%{with_system_tex4ht}
    ln -sf ht		../share/texmf-dist/scripts/tex4ht/ht.sh
    ln -sf htcontext	../share/texmf-dist/scripts/tex4ht/htcontext.sh
    ln -sf htlatex	../share/texmf-dist/scripts/tex4ht/htlatex.sh
    ln -sf htmex	../share/texmf-dist/scripts/tex4ht/htmex.sh
    ln -sf httex	../share/texmf-dist/scripts/tex4ht/httex.sh
    ln -sf httexi	../share/texmf-dist/scripts/tex4ht/httexi.sh
    ln -sf htxelatex	../share/texmf-dist/scripts/tex4ht/htxelatex.sh
    ln -sf htxetex	../share/texmf-dist/scripts/tex4ht/htxetex.sh
%endif
    ln -sf latex2man	../share/texmf-dist/scripts/latex2man/latex2man
    ln -sf latexdiff	../share/texmf-dist/scripts/latexdiff/latexdiff.pl
    ln -sf latexdiff-vc	../share/texmf-dist/scripts/latexdiff/latexdiff-vc.pl
    ln -sf latexmk	../share/texmf-dist/scripts/latexmk/latexmk.pl
    ln -sf latexrevise	../share/texmf-dist/scripts/latexdiff/latexrevise.pl
    ln -sf listings-ext.sh	../share/texmf-dist/scripts/listings-ext/listings-ext.sh
    ln -sf makeglossaries	../share/texmf-dist/scripts/glossaries/makeglossaries
    ln -sf mathspic	../share/texmf-dist/scripts/mathspic/mathspic.pl
%if !%{with_system_tex4ht}
    ln -sf mk4ht	../share/texmf-dist/scripts/tex4ht/mk4ht.pl
%endif
    ln -sf mkgrkindex	../share/texmf-dist/scripts/mkgrkindex/mkgrkindex
    ln -sf mkjobtexmf	../share/texmf-dist/scripts/mkjobtexmf/mkjobtexmf.pl
    ln -sf mkluatexfontdb	../share/texmf-dist/scripts/luaotfload/mkluatexfontdb.lua
    ln -sf mkt1font	../share/texmf-dist/scripts/accfonts/mkt1font
    ln -sf mptopdf	../share/texmf-dist/scripts/context/perl/mptopdf.pl
    ln -sf ot2kpx	../share/texmf-dist/scripts/fontools/ot2kpx
    ln -sf pdf180	../share/texmf-dist/scripts/pdfjam/pdf180
    ln -sf pdf270	../share/texmf-dist/scripts/pdfjam/pdf270
    ln -sf pdf90	../share/texmf-dist/scripts/pdfjam/pdf90
    ln -sf pdfannotextractor	../share/texmf-dist/scripts/pax/pdfannotextractor.pl
    ln -sf pdfatfi	../share/texmf-dist/scripts/oberdiek/pdfatfi.pl
    ln -sf pdfbook	../share/texmf-dist/scripts/pdfjam/pdfbook
    ln -sf pdfcrop	../share/texmf-dist/scripts/pdfcrop/pdfcrop.pl
    ln -sf pdfflip	../share/texmf-dist/scripts/pdfjam/pdfflip
    ln -sf pdfjam	../share/texmf-dist/scripts/pdfjam/pdfjam
    ln -sf pdfjam-pocketmod	../share/texmf-dist/scripts/pdfjam/pdfjam-pocketmod
    ln -sf pdfjam-slides3up	../share/texmf-dist/scripts/pdfjam/pdfjam-slides3up
    ln -sf pdfjam-slides6up	../share/texmf-dist/scripts/pdfjam/pdfjam-slides6up
    ln -sf pdfjoin	../share/texmf-dist/scripts/pdfjam/pdfjoin
    ln -sf pdfnup	../share/texmf-dist/scripts/pdfjam/pdfnup
    ln -sf pdfpun	../share/texmf-dist/scripts/pdfjam/pdfpun
    ln -sf pdfthumb	../share/texmf-dist/scripts/ppower4/pdfthumb.tlu
    ln -sf perltex	../share/texmf-dist/scripts/perltex/perltex.pl
    ln -sf pfm2kpx	../share/texmf-dist/scripts/fontools/pfm2kpx
    ln -sf pkfix	../share/texmf-dist/scripts/pkfix/pkfix.pl
    ln -sf pkfix-helper	../share/texmf-dist/scripts/pkfix-helper/pkfix-helper
    ln -sf ppower4	../share/texmf-dist/scripts/ppower4/ppower4.tlu
    ln -sf ps4pdf	../share/texmf-dist/scripts/pst-pdf/ps4pdf
    ln -sf pst2pdf	../share/texmf-dist/scripts/pst2pdf/pst2pdf
    ln -sf purifyeps	../share/texmf-dist/scripts/purifyeps/purifyeps
    ln -sf repstopdf	epstopdf
    ln -sf rpdfcrop	pdfcrop
    ln -sf rungs	../share/texmf/scripts/texlive/rungs.tlu
    ln -sf showglyphs	../share/texmf-dist/scripts/fontools/showglyphs
    ln -sf splitindex	../share/texmf-dist/scripts/splitindex/perl/splitindex.pl
    ln -sf simpdftex	../share/texmf/scripts/simpdftex/simpdftex
    ln -sf svn-multi	../share/texmf-dist/scripts/svn-multi/svn-multi.pl
    ln -sf texcount	../share/texmf-dist/scripts/texcount/texcount.pl
    ln -sf texdiff	../share/texmf-dist/scripts/texdiff/texdiff
    ln -sf texdirflatten	../share/texmf-dist/scripts/texdirflatten/texdirflatten
    ln -sf texdoc	../share/texmf/scripts/texdoc/texdoc.tlu
    ln -sf texloganalyser	../share/texmf-dist/scripts/texloganalyser/texloganalyser
    ln -sf thumbpdf	../share/texmf-dist/scripts/thumbpdf/thumbpdf.pl
    ln -sf ulqda	../share/texmf-dist/scripts/ulqda/ulqda.pl
    ln -sf vpe	../share/texmf-dist/scripts/vpe/vpe.pl
    ln -sf vpl2ovp	../share/texmf-dist/scripts/accfonts/vpl2ovp
    ln -sf vpl2vpl	../share/texmf-dist/scripts/accfonts/vpl2vpl
popd

mkdir -p %{buildroot}%{_datadir}/fonts
pushd %{buildroot}%{_datadir}/fonts
    ln -sf texmf	../texmf/fonts
    ln -sf texmf-dist	../texmf-dist/fonts
popd

mkdir -p %{buildroot}%{_datadir}/X11/app-defaults
pushd %{buildroot}%{_datadir}/X11/app-defaults
    ln -sf XDvi		../texmf/xdvi/XDvi
fi

pushd %{buildroot}%{_datadir}/texmf
%if !%{enable_asymptote}
    rm -fr asymptote doc/asymptote
%endif
%if !%{enable_xindy}
    rm -fr xindy doc/xindy scripts/xindy
%endif
    rm -fr dvipdfm
    perl -pi -e 's%/usr/local%/usr%;' dvipdfmx/dvipdfmx.cfg
    rm -f ls-R README
popd

pushd %{buildroot}%{_datadir}/texmf-dist
%if %{with_system_tex4ht}
    rm -fr tex4ht
%endif
    rm -f ls-R README
popd

#-----------------------------------------------------------------------
%clean
rm -rf %{buildroot}
