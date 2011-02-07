# FIXME temporary hack for test builds
%define __find_provides		%{nil}
%define __find_requires		%{nil}

Name:		texlive-texmf
Version:	20100722
Release:	%mkrel 1
Summary:	Architecture independent parts of the TeX formatting system
Group:		Publishing
License:	Artistic 2.0 and GPLv2 and GPLv2+ and LGPLv2+ and LPPL and MIT and Public Domain and UCD and Utopia
URL:		http://tug.org/texlive/
Source0:	ftp://tug.org/historic/systems/texlive/2010/texlive-20100722-texmf.tar.xz
Source1:	ftp://tug.org/historic/systems/texlive/2010/texlive-20100722-texmf.tar.xz.sha256
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch
Requires:	perl-Algorithm-Diff

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

%description
texlive-texmf is a texmf distribution based upon TeX Live. All of the files
contained in these packages are from the TeX Live zip files. The intent is to
provide a packaging similar in style and layout to teTeX.

%files
%defattr(-,root,root,-)
%{_datadir}/texmf/*
%exclude %{_datadir}/texmf/doc
%{_datadir}/texmf-dist/*
%exclude %{_datadir}/texmf-dist/doc

#-----------------------------------------------------------------------
%package	doc
Summary:	TeX Live documentation
Group:		Publishing
Requires:	texlive-doc = %{version}

%description	doc
texlive-texmf is a texmf distribution based upon TeX Live. All of the files
contained in these packages are from the TeX Live zip files. The intent is to
provide a packaging similar in style and layout to teTeX.

%files		doc
%defattr(-,root,root,-)
%{_datadir}/texmf/doc/*
%{_datadir}/texmf-dist/doc/*

#-----------------------------------------------------------------------
%prep
%setup -q -n texlive-20100722-texmf

perl -pi -e 's%^(TEXMFMAIN\s+= ).*%$1%{_datadir}/texmf%;'					 \
	 -e 's%^(TEXMFLOCAL\s+= ).*%$1\{%{_datadir}/texmf-local,%{_datadir}/texmf\}%;'		 \
	 -e 's%^(TEXMFFONTS\s+= ).*%$1\{%{_datadir}/texmf/fonts,%{_datadir}/texmf-dist/fonts\}%;'\
	 -e 's%^(TEXMFEXTRA\s+= ).*%$1\{%{_datadir}/texmf-extra,%{_datadir}/texmf\}%;'		 \
	 -e 's%^(TEXMFPROJECT\s+= ).*%$1\{%{_datadir}/texmf-project,%{_datadir}/texmf\}%;'	 \
	 -e 's%^(VARTEXMF\s+= ).*%$1\$HOME/.texlive2010/texmf-var%;'				 \
	 -e 's%^(HOMETEXMF\s+= ).*%$1\{\$HOME/texmf,%{_datadir}/texmf\}%;'			 \
	 -e 's%^(TEXMFCNF\s+= ).*%$1%{_datadir}/texmf/web2c%;'					 \
	texmf/web2c/context.cnf

#-----------------------------------------------------------------------
%build
# not really, just make "--short-circuit -bi" easier to "debug"
mkdir -p %{buildroot}%{_datadir}
cp -far * %{buildroot}%{_datadir}

#-----------------------------------------------------------------------
%install

# files generated by texlive package
pushd %{buildroot}%{_datadir}/texmf
    rm -fr chktex
    rm -fr doc/bibtex8
    rm -fr doc/chktex
    rm -fr doc/tetex
    rm -fr dvipdfmx
    rm -fr dvips/base
    rm -fr dvips/gsftopk
    rm -f fonts/cmap/dvipdfmx/EUC-UCS2
    rm -f scripts/tetex/texdoctk.pl
    rm -f scripts/texlive/tlmgr.pl
    rm -fr texconfig
    rm -fr web2c/fmtutil.cnf
    rm -fr web2c/mktexdir
    rm -fr web2c/mktexdir.opt
    rm -fr web2c/mktexnam
    rm -fr web2c/mktexnam.opt
    rm -fr web2c/mktexupd
    rm -fr web2c/texmf.cnf
    rm -fr xdvi
popd

pushd %{buildroot}%{_datadir}/texmf-dist
    rm -fr bibtex/csf/base
    rm -f fonts/enc/dvips/base/7t.enc
    rm -fr fonts/map/glyphlist
    rm -fr scripts/accfonts
    rm -fr scripts/authorindex
    rm -fr scripts/bengali
    rm -fr scripts/bibexport
    rm -fr scripts/bundledoc
    rm -f scripts/cachepic/cachepic.cmd
    rm -f scripts/context/perl/mptopdf.pl
    rm -fr scripts/de-macro
    rm -fr scripts/dviasm
    rm -f scripts/epspdf/epspdf
    rm -f scripts/epspdf/epspdftk
    rm -fr scripts/epstopdf
    rm -fr scripts/fig4latex
    rm -fr scripts/findhyph
    rm -fr scripts/fontools
    rm -fr scripts/fragmaster
    rm -f scripts/glossaries/makeglossaries
    rm -fr scripts/latex2man
    rm -fr scripts/latexdiff
    rm -fr scripts/latexmk
    rm -fr scripts/listings-ext
    rm -fr scripts/luaotfload
    rm -fr scripts/mathspic
    rm -fr scripts/mkgrkindex
    rm -f scripts/oberdiek/pdfatfi.pl
    rm -f scripts/pax/pdfannotextractor.pl
    rm -fr scripts/pdfcrop
    rm -fr scripts/pdfjam
    rm -fr scripts/perltex
    rm -fr scripts/pkfix
    rm -fr scripts/pkfix-helper
    rm -f scripts/ppower4/pdfthumb.tlu
    rm -f scripts/ppower4/ppower4.tlu
    rm -fr scripts/pst2pdf
    rm -f scripts/pst-pdf/ps4pdf
    rm -fr scripts/purifyeps
    rm -fr scripts/splitindex
    rm -fr scripts/svn-multi
    rm -fr scripts/tex4ht
    rm -fr scripts/texcount
    rm -fr scripts/texdiff
    rm -fr scripts/texdirflatten
    rm -fr scripts/texloganalyser
    rm -fr scripts/thumbpdf
    rm -fr scripts/ulqda
    rm -fr scripts/vpe
popd

#-----------------------------------------------------------------------
%clean
# FIXME temporary hack for test builds
%if 0
rm -rf %{buildroot}
%endif
