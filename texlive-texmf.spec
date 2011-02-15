#%#define __find_provides		%{nil}
#%#define __find_requires		%{nil}
#%#define __find_lang		%{nil}

%define __spec_install_pre	export RPM_SOURCE_DIR="%{_sourcedir}";export RPM_BUILD_DIR="%{_builddir}";export RPM_OPT_FLAGS="%{optflags}";export RPM_ARCH="%{_arch}";export RPM_OS="%{_os}";export RPM_DOC_DIR="%%{_docdir}";export RPM_PACKAGE_NAME="%%{name}";export RPM_PACKAGE_VERSION="%%{version}";export RPM_PACKAGE_RELEASE="%%{release}";export RPM_BUILD_ROOT="%{buildroot}";export LC_ALL=C;export LANG=C;cd %_builddir
%define enable_asymptote	1
%define enable_xindy		1

%define with_system_dialog	1
%define with_system_lcdf	0
%define with_system_poppler	0
%define with_system_psutils	1
%define with_system_t1lib	1
%define with_system_tex4ht	0
%define with_system_teckit	0

Name:		texlive-texmf
Version:	20100722
Release:	%mkrel 2
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

%if %mdkversion <= 201100
Provides:	texlive-texmf-common = %{version}
Provides:	texlive-texmf-context = %{version}
Provides:	texlive-texmf-dvipdfm = %{version}
Provides:	texlive-texmf-dvips = %{version}
Provides:	texlive-texmf-jadetex = %{version}
Provides:	texlive-texmf-latex = %{version}
Provides:	texlive-texmf-usrlocal = %{version}
Provides:	texlive-texmf-xmltex = %{version}
Provides:	texmf-data = %{version}
%endif

Obsoletes:	texlive-texmf-common <= 2007
Obsoletes:	texlive-texmf-context <= 2007
Obsoletes:	texlive-texmf-dvipdfm <= 2007
Obsoletes:	texlive-texmf-dvips <= 2007
Obsoletes:	texlive-texmf-jadetex <= 2007
Obsoletes:	texlive-texmf-latex <= 2007
Obsoletes:	texlive-texmf-usrlocal <= 2007
Obsoletes:	texlive-texmf-xmltex <= 2007
Obsoletes:	texmf-data <= 2007

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
%dir %{_datadir}/texmf/doc
%if %{enable_asymptote}
%{_datadir}/texmf/asymptote
%doc %{_datadir}/texmf/doc/asymptote
%endif
%{_datadir}/texmf/dvipdfmx
%{_datadir}/texmf/dvips
%{_datadir}/texmf/hbf2gf
%{_datadir}/texmf/scripts
%{_datadir}/texmf/tex
%{_datadir}/texmf/texconfig
%{_datadir}/texmf/texdoc
%{_datadir}/texmf/texdoctk
%{_datadir}/texmf/ttf2pk
%{_datadir}/texmf/web2c
%{_datadir}/texmf/xdvi
%if %{enable_xindy}
%{_datadir}/texmf/xindy
%doc %{_datadir}/texmf/doc/xindy
%endif
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
%{_datadir}/texmf/doc/*
%if %{enable_asymptote}
%exclude %{_datadir}/texmf/doc/asymptote
%endif
%if %{enable_xindy}
%exclude %{_datadir}/texmf/doc/xindy
%endif
%{_datadir}/texmf-dist/doc

#-----------------------------------------------------------------------
%package	-n texlive-fonts
Summary:	Tex Live fonts
Group:		Publishing
%if %mdkversion <= 201100
Provides:	textex-cmsuper = %{version}
Provides:	texlive-texmf-afm = %{version}
Provides:	texlive-texmf-cmsuper = %{version}
Provides:	texlive-texmf-fonts = %{version}-%{release}
%endif
Obsoletes:	textex-cmsuper <= 0.3.3
Obsoletes:	texlive-texmf-fonts <= 2007
Obsoletes:	texlive-texmf-afm <= 2007
Obsoletes:	texlive-texmf-cmsuper <= 2007

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

perl -pi -e 's%^(TEXMFMAIN\s+= ).*%$1%{_datadir}/texmf%;'			\
	 -e 's%^(TEXMFDIST\s+= ).*%$1%{_datadir}/texmf-dist%;'			\
	 -e 's%^(TEXMFLOCAL\s+= ).*%$1%{_datadir}/texmf%;'			\
	 -e 's%^(TEXMFSYSVAR\s+= ).*%$1%{_localstatedir}/lib/texmf%;'		\
	 -e 's%^(TEXMFSYSCONFIG\s+= ).*%$1%{_sysconfdir}/texmf%;'		\
	 -e 's%^(TEXMFHOME\s+= ).*%$1\{\$HOME/texmf,%{_datadir}/texmf\}%;'	\
	 -e 's%^(TEXMFVAR\s+= ).*%$1\$HOME/.texlive2010/texmf-var%;'		\
	 -e 's%^(TEXMFCONFIG\s+= ).*%$1\$HOME/.texlive2010/texmf-config%;'	\
	 -e 's%^(OSFONTDIR\s+= ).*%$1%{_datadir}/fonts%;'			\
	texmf/web2c/texmf.cnf

perl -pi -e 's%^(TEXMFMAIN\s+= ).*%$1%{_datadir}/texmf%;'					 \
	 -e 's%^(TEXMFLOCAL\s+= ).*%$1%{_datadir}/texmf%;'					 \
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

#-----------------------------------------------------------------------
%install
mkdir -p %{buildroot}%{_datadir}
cp -far * %{buildroot}%{_datadir}

mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
    ln -sf ../share/texmf/scripts/a2ping/a2ping.pl a2ping
    ln -sf ../share/texmf-dist/scripts/fontools/afm2afm afm2afm
    ln -sf ../share/texmf-dist/scripts/bundledoc/arlatex arlatex
    ln -sf ../share/texmf-dist/scripts/authorindex/authorindex authorindex
    ln -sf ../share/texmf-dist/scripts/fontools/autoinst autoinst
    ln -sf ../share/texmf-dist/scripts/bibexport/bibexport.sh bibexport
    ln -sf ../share/texmf-dist/scripts/bundledoc/bundledoc bundledoc
    ln -sf ../share/texmf-dist/scripts/cachepic/cachepic.tlu cachepic
    ln -sf ../share/texmf-dist/scripts/fontools/cmap2enc cmap2enc
    ln -sf ../share/texmf-dist/scripts/de-macro/de-macro de-macro
    ln -sf ../share/texmf-dist/scripts/dviasm/dviasm.py dviasm
    ln -sf ../share/texmf/scripts/tetex/e2pall.pl e2pall
    ln -sf ../share/texmf-dist/scripts/bengali/ebong.py ebong
    ln -sf ../share/texmf-dist/scripts/epspdf/epspdf epspdf
    ln -sf ../share/texmf-dist/scripts/epspdf/epspdftk epspdftk
    ln -sf ../share/texmf-dist/scripts/epstopdf/epstopdf.pl epstopdf
    ln -sf ../share/texmf-dist/scripts/fig4latex/fig4latex fig4latex
    ln -sf ../share/texmf-dist/scripts/findhyph/findhyph findhyph
    ln -sf ../share/texmf-dist/scripts/fontools/font2afm font2afm
    ln -sf ../share/texmf-dist/scripts/fragmaster/fragmaster.pl fragmaster
%if !%{with_system_tex4ht}
    ln -sf ../share/texmf-dist/scripts/tex4ht/ht.sh ht
    ln -sf ../share/texmf-dist/scripts/tex4ht/htcontext.sh htcontext
    ln -sf ../share/texmf-dist/scripts/tex4ht/htlatex.sh htlatex
    ln -sf ../share/texmf-dist/scripts/tex4ht/htmex.sh htmex
    ln -sf ../share/texmf-dist/scripts/tex4ht/httex.sh httex
    ln -sf ../share/texmf-dist/scripts/tex4ht/httexi.sh httexi
    ln -sf ../share/texmf-dist/scripts/tex4ht/htxelatex.sh htxelatex
    ln -sf ../share/texmf-dist/scripts/tex4ht/htxetex.sh htxetex
%endif
    ln -sf ../share/texmf-dist/scripts/latex2man/latex2man latex2man
    ln -sf ../share/texmf-dist/scripts/latexdiff/latexdiff.pl latexdiff
    ln -sf ../share/texmf-dist/scripts/latexdiff/latexdiff-vc.pl latexdiff-vc
    ln -sf ../share/texmf-dist/scripts/latexmk/latexmk.pl latexmk
    ln -sf ../share/texmf-dist/scripts/latexdiff/latexrevise.pl latexrevise
    ln -sf ../share/texmf-dist/scripts/listings-ext/listings-ext.sh listings-ext.sh
    ln -sf ../share/texmf-dist/scripts/glossaries/makeglossaries makeglossaries
    ln -sf ../share/texmf-dist/scripts/mathspic/mathspic.pl mathspic
%if !%{with_system_tex4ht}
    ln -sf ../share/texmf-dist/scripts/tex4ht/mk4ht.pl mk4ht
%endif
    ln -sf ../share/texmf-dist/scripts/mkgrkindex/mkgrkindex mkgrkindex
    ln -sf ../share/texmf-dist/scripts/mkjobtexmf/mkjobtexmf.pl mkjobtexmf
    ln -sf ../share/texmf-dist/scripts/luaotfload/mkluatexfontdb.lua mkluatexfontdb
    ln -sf ../share/texmf-dist/scripts/accfonts/mkt1font mkt1font
    ln -sf ../share/texmf-dist/scripts/context/perl/mptopdf.pl mptopdf
    ln -sf ../share/texmf-dist/scripts/fontools/ot2kpx ot2kpx
    ln -sf ../share/texmf-dist/scripts/pdfjam/pdf180 pdf180
    ln -sf ../share/texmf-dist/scripts/pdfjam/pdf270 pdf270
    ln -sf ../share/texmf-dist/scripts/pdfjam/pdf90 pdf90
    ln -sf ../share/texmf-dist/scripts/pax/pdfannotextractor.pl pdfannotextractor
    ln -sf ../share/texmf-dist/scripts/oberdiek/pdfatfi.pl pdfatfi
    ln -sf ../share/texmf-dist/scripts/pdfjam/pdfbook pdfbook
    ln -sf ../share/texmf-dist/scripts/pdfcrop/pdfcrop.pl pdfcrop
    ln -sf ../share/texmf-dist/scripts/pdfjam/pdfflip pdfflip
    ln -sf ../share/texmf-dist/scripts/pdfjam/pdfjam pdfjam
    ln -sf ../share/texmf-dist/scripts/pdfjam/pdfjam-pocketmod pdfjam-pocketmod
    ln -sf ../share/texmf-dist/scripts/pdfjam/pdfjam-slides3up pdfjam-slides3up
    ln -sf ../share/texmf-dist/scripts/pdfjam/pdfjam-slides6up pdfjam-slides6up
    ln -sf ../share/texmf-dist/scripts/pdfjam/pdfjoin pdfjoin
    ln -sf ../share/texmf-dist/scripts/pdfjam/pdfnup pdfnup
    ln -sf ../share/texmf-dist/scripts/pdfjam/pdfpun pdfpun
    ln -sf ../share/texmf-dist/scripts/ppower4/pdfthumb.tlu pdfthumb
    ln -sf ../share/texmf-dist/scripts/perltex/perltex.pl perltex
    ln -sf ../share/texmf-dist/scripts/fontools/pfm2kpx pfm2kpx
    ln -sf ../share/texmf-dist/scripts/pkfix/pkfix.pl pkfix
    ln -sf ../share/texmf-dist/scripts/pkfix-helper/pkfix-helper pkfix-helper
    ln -sf ../share/texmf-dist/scripts/ppower4/ppower4.tlu ppower4
    ln -sf ../share/texmf-dist/scripts/pst-pdf/ps4pdf ps4pdf
    ln -sf ../share/texmf-dist/scripts/pst2pdf/pst2pdf pst2pdf
    ln -sf ../share/texmf-dist/scripts/purifyeps/purifyeps purifyeps
    ln -sf epstopdf repstopdf
    ln -sf pdfcrop rpdfcrop
    ln -sf ../share/texmf/scripts/texlive/rungs.tlu rungs
    ln -sf ../share/texmf-dist/scripts/fontools/showglyphs showglyphs
    ln -sf ../share/texmf-dist/scripts/splitindex/perl/splitindex.pl splitindex
    ln -sf ../share/texmf/scripts/simpdftex/simpdftex simpdftex
    ln -sf ../share/texmf-dist/scripts/svn-multi/svn-multi.pl svn-multi
    ln -sf ../share/texmf-dist/scripts/texcount/texcount.pl texcount
    ln -sf ../share/texmf-dist/scripts/texdiff/texdiff texdiff
    ln -sf ../share/texmf-dist/scripts/texdirflatten/texdirflatten texdirflatten
    ln -sf ../share/texmf/scripts/texdoc/texdoc.tlu texdoc
    ln -sf ../share/texmf-dist/scripts/texloganalyser/texloganalyser texloganalyser
    ln -sf ../share/texmf-dist/scripts/thumbpdf/thumbpdf.pl thumbpdf
    ln -sf ../share/texmf-dist/scripts/ulqda/ulqda.pl ulqda
    ln -sf ../share/texmf-dist/scripts/vpe/vpe.pl vpe
    ln -sf ../share/texmf-dist/scripts/accfonts/vpl2ovp vpl2ovp
    ln -sf ../share/texmf-dist/scripts/accfonts/vpl2vpl vpl2vpl
popd

mkdir -p %{buildroot}%{_datadir}/fonts
pushd %{buildroot}%{_datadir}/fonts
    ln -sf ../texmf/fonts texmf
    ln -sf ../texmf-dist/fonts texmf-dist
popd

mkdir -p %{buildroot}%{_datadir}/X11/app-defaults
pushd %{buildroot}%{_datadir}/X11/app-defaults
    ln -sf ../../texmf/xdvi/XDvi XDvi
popd

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
    rm -fr doc/gzip
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
