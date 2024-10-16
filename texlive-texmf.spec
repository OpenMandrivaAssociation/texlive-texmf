%define _binary_payload		w9.gzdio
%define _source_payload		w9.gzdio

%define _requires_exceptions	perl(Text::Unidecode)\\|perl(Tie::Watch)\\|perl(SelfLoader)

%define enable_asymptote	0
%define enable_xindy		0

%define with_system_dialog	1
%define with_system_lcdf	0
%define with_system_poppler	0
%define with_system_psutils	1
%define with_system_t1lib	1
%define with_system_tex4ht	0
%define with_system_teckit	0

%if %mdkversion >= 201100
  %define texmfbindir		%{_bindir}
  %define texmfdir		%{_datadir}/texmf
  %define texmfdistdir		%{_datadir}/texmf-dist
  %define texmflocaldir		%{_datadir}/texmf-local
  %define texmfextradir		%{_datadir}/texmf-extra
  %define texmffontsdir		%{_datadir}/texmf-fonts
  %define texmfprojectdir	%{_datadir}/texmf-project
  %define texmfvardir		%{_localstatedir}/lib/texmf
  %define texmfconfdir		%{_sysconfdir}/texmf
%else
  %define texmfbindir		/opt/texlive2011/bin
  %define texmfdir		/opt/texlive2011/texmf
  %define texmfdistdir		/opt/texlive2011/texmf-dist
  %define texmflocaldir		/opt/texlive2011/texmf-local
  %define texmfextradir		/opt/texlive2011/texmf-extra
  %define texmffontsdir		/opt/texlive2011/texmf-fonts
  %define texmfprojectdir	/opt/texlive2011/texmf-project
  %define texmfdistdir		/opt/texlive2011/texmf-dist
  %define texmfvardir		/opt/texlive2011/lib/texmf
  %define texmfconfdir		/opt/texlive2011/texmf
%endif

Name:		texlive-texmf
Version:	20110705
Release:	%mkrel 3
Summary:	The TeX formatting system
Group:		Publishing
License:	http://www.tug.org/texlive/LICENSE.TL
URL:		https://tug.org/texlive/
Source0:	ftp://tug.org/historic/systems/texlive/2011/texlive-20110705-texmf.tar.xz
Source1:	ftp://tug.org/historic/systems/texlive/2011/texlive-20110705-texmf.tar.xz.sha256
Source2:	XDvi-color
Source3:	http://www.tug.org/texlive/LICENSE.TL
Source4:	http://mirror.ctan.org/systems/texlive/tlnet/install-tl-unx.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch

#-----------------------------------------------------------------------
Requires:	perl-Algorithm-Diff
Requires(post):	/sbin/install-info
Requires(preun): /sbin/install-info
Requires:	xdg-utils

%if %mdkversion <= 201200
Provides:	tetex-afm = %{version}
Provides:	tetex-cmsuper = %{version}
%if !%{with_system_tex4ht}
Provides:	tex4ht = 1:%{version}
%endif
Provides:	texlive-fonts = %{version}
Provides:	texlive-texmf-afm = %{version}
Provides:	texlive-texmf-cmsuper = %{version}
Provides:	texlive-texmf-common = %{version}
Provides:	texlive-texmf-context = %{version}
Provides:	texlive-texmf-dvipdfm = %{version}
Provides:	texlive-texmf-dvips = %{version}
Provides:	texlive-texmf-fonts = %{version}
Provides:	texlive-texmf-jadetex = %{version}
Provides:	texlive-texmf-latex = %{version}
Provides:	texlive-texmf-usrlocal = %{version}
Provides:	texlive-texmf-xmltex = %{version}
Provides:	texmf-data = %{version}
%endif
%if %mdkversion >= 201100
Obsoletes:	tetex-afm <= 3.0
Obsoletes:	tetex-cmsuper <= 0.3.3
%if !%{with_system_tex4ht}
Obsoletes:	tex4ht <= 1:1.0.2008_02_28_2058
%endif
Obsoletes:	texlive-fonts <= 2007
Obsoletes:	texlive-texmf-afm <= 2007
Obsoletes:	texlive-texmf-fonts <= 2007
Obsoletes:	texlive-texmf-cmsuper <= 2007
Obsoletes:	texlive-texmf-common <= 2007
Obsoletes:	texlive-texmf-context <= 2007
Obsoletes:	texlive-texmf-dvipdfm <= 2007
Obsoletes:	texlive-texmf-dvips <= 2007
Obsoletes:	texlive-texmf-jadetex <= 2007
Obsoletes:	texlive-texmf-latex <= 2007
Obsoletes:	texlive-texmf-usrlocal <= 2007
Obsoletes:	texlive-texmf-xmltex <= 2007
Obsoletes:	texmf-data <= 2007
%endif

Conflicts:	texlive-doc < %{version}-%{release}
Conflicts:	texlive-fontsextra < %{version}-%{release}
Conflicts:	texlive-source < %{version}-%{release}

#-----------------------------------------------------------------------
Patch0:		texlive-20110705-texmf-default.patch
Patch1:		texlive-20110705-texmf-fontsextra.patch
Patch2:		texlive-20110705-texmf-epstopdf.patch
# http://tug.org/svn/texlive/trunk/Master/texmf-dist/tex/context/base/type-one.mkii?r1=23189&r2=23188&pathrev=23189
Patch3:		texlive-20110705-texmf-context-hotfixes.patch

#-----------------------------------------------------------------------
%description
TeX Live is an easy way to get up and running with the TeX document
production system. It provides a comprehensive TeX system. It includes
all the major TeX-related programs, macro packages, and fonts that are
free software, including support for many languages around the world.

%files
%defattr(-,root,root,-)
%{texmfbindir}/*
%if %mdkversion >= 201100
%{_datadir}/X11/app-defaults/XDvi*
%{_infodir}/*
%{_mandir}/man1/*
%{_mandir}/man5/*
%endif
%dir %{texmfdir}
%{texmfdir}/chktex
%dir %{texmfdir}/doc
%{texmfdir}/doc/tetex
%if %{enable_asymptote}
%{texmfdir}/asymptote
%doc %{texmfdir}/doc/asymptote
%endif
%{texmfdir}/dvipdfmx
%{texmfdir}/dvips
%{texmfdir}/fonts
%{texmfdir}/hbf2gf
%{texmfdir}/LICENSE.TL
%{texmfdir}/scripts
%{texmfdir}/tex
%{texmfdir}/texconfig
%{texmfdir}/texdoctk
%{texmfdir}/tlpkg
%{texmfdir}/ttf2pk
%{texmfdir}/web2c
%{texmfdir}/xdvi
%if %{enable_xindy}
%{texmfdir}/xindy
%doc %{texmfdir}/doc/xindy
%endif
%dir %{texmfdistdir}
%{texmfdistdir}/bibtex
%{texmfdistdir}/context
%{texmfdistdir}/dvips
%{texmfdistdir}/fonts

# collection-fontsextra
# allrunes
%exclude %{texmfdistdir}/fonts/map/dvips/allrunes
%exclude %{texmfdistdir}/fonts/source/public/allrunes
%exclude %{texmfdistdir}/fonts/type1/public/allrunes
%exclude %{texmfdistdir}/tex/latex/allrunes
# antiqua
%exclude %{texmfdistdir}/dvips/antiqua
%exclude %{texmfdistdir}/fonts/afm/urw/antiqua
%exclude %{texmfdistdir}/fonts/map/dvips/antiqua
%exclude %{texmfdistdir}/fonts/tfm/urw/antiqua
%exclude %{texmfdistdir}/fonts/type1/urw/antiqua
%exclude %{texmfdistdir}/fonts/vf/urw/antiqua
%exclude %{texmfdistdir}/tex/latex/antiqua
# antt
%exclude %{texmfdistdir}/fonts/afm/public/antt
%exclude %{texmfdistdir}/fonts/enc/dvips/antt
%exclude %{texmfdistdir}/fonts/map/dvips/antt
%exclude %{texmfdistdir}/fonts/opentype/public/antt
%exclude %{texmfdistdir}/fonts/tfm/public/antt
%exclude %{texmfdistdir}/fonts/type1/public/antt
%exclude %{texmfdistdir}/tex/latex/antt
%exclude %{texmfdistdir}/tex/plain/antt
# ar
%exclude %{texmfdistdir}/fonts/source/public/ar
%exclude %{texmfdistdir}/fonts/tfm/public/ar
%exclude %{texmfdistdir}/tex/latex/ar
# archaic
%exclude %{texmfdistdir}/fonts/afm/public/archaic
%exclude %{texmfdistdir}/fonts/map/dvips/archaic
%exclude %{texmfdistdir}/fonts/source/public/archaic
%exclude %{texmfdistdir}/fonts/tfm/public/archaic
%exclude %{texmfdistdir}/fonts/type1/public/archaic
%exclude %{texmfdistdir}/tex/latex/archaic
# arev
%exclude %{texmfdistdir}/fonts/afm/public/arev
%exclude %{texmfdistdir}/fonts/enc/dvips/arev
%exclude %{texmfdistdir}/fonts/map/dvips/arev
%exclude %{texmfdistdir}/fonts/tfm/public/arev
%exclude %{texmfdistdir}/fonts/type1/public/arev
%exclude %{texmfdistdir}/fonts/vf/public/arev
%exclude %{texmfdistdir}/tex/latex/arev
# ascii
%exclude %{texmfdistdir}/fonts/map/dvips/ascii
%exclude %{texmfdistdir}/fonts/tfm/public/ascii
%exclude %{texmfdistdir}/fonts/type1/public/ascii
%exclude %{texmfdistdir}/tex/latex/ascii
# astro
%exclude %{texmfdistdir}/fonts/source/public/astro
%exclude %{texmfdistdir}/fonts/tfm/public/astro
# augie
%exclude %{texmfdistdir}/fonts/afm/public/augie
%exclude %{texmfdistdir}/fonts/map/dvips/augie
%exclude %{texmfdistdir}/fonts/tfm/public/augie
%exclude %{texmfdistdir}/fonts/type1/public/augie
%exclude %{texmfdistdir}/fonts/vf/public/augie
%exclude %{texmfdistdir}/tex/latex/augie
# auncial-new
%exclude %{texmfdistdir}/fonts/afm/public/auncial-new
%exclude %{texmfdistdir}/fonts/map/dvips/auncial-new
%exclude %{texmfdistdir}/fonts/tfm/public/auncial-new
%exclude %{texmfdistdir}/fonts/type1/public/auncial-new
%exclude %{texmfdistdir}/tex/latex/auncial-new
# aurical
%exclude %{texmfdistdir}/fonts/afm/public/aurical
%exclude %{texmfdistdir}/fonts/map/dvips/aurical
%exclude %{texmfdistdir}/fonts/source/public/aurical
%exclude %{texmfdistdir}/fonts/tfm/public/aurical
%exclude %{texmfdistdir}/fonts/type1/public/aurical
%exclude %{texmfdistdir}/tex/latex/aurical
# barcodes
%exclude %{texmfdistdir}/fonts/source/public/barcodes
%exclude %{texmfdistdir}/fonts/tfm/public/barcodes
%exclude %{texmfdistdir}/tex/latex/barcodes
# baskervald
%exclude %{texmfdistdir}/fonts/afm/arkandis/baskervald
%exclude %{texmfdistdir}/fonts/enc/dvips/baskervald
%exclude %{texmfdistdir}/fonts/map/dvips/baskervald
%exclude %{texmfdistdir}/fonts/tfm/arkandis/baskervald
%exclude %{texmfdistdir}/fonts/type1/arkandis/baskervald
%exclude %{texmfdistdir}/fonts/vf/arkandis/baskervald
%exclude %{texmfdistdir}/tex/latex/baskervald
# bbding
%exclude %{texmfdistdir}/fonts/source/public/bbding
%exclude %{texmfdistdir}/fonts/tfm/public/bbding
%exclude %{texmfdistdir}/tex/latex/bbding
# bbm
%exclude %{texmfdistdir}/fonts/source/public/bbm
%exclude %{texmfdistdir}/fonts/tfm/public/bbm
# bbm-macros
%exclude %{texmfdistdir}/tex/latex/bbm-macros
# bbold
%exclude %{texmfdistdir}/fonts/source/public/bbold
%exclude %{texmfdistdir}/fonts/tfm/public/bbold
%exclude %{texmfdistdir}/tex/latex/bbold
# belleek
%exclude %{texmfdistdir}/fonts/map/dvips/belleek
%exclude %{texmfdistdir}/fonts/truetype/public/belleek
%exclude %{texmfdistdir}/fonts/type1/public/belleek
# bera
%exclude %{texmfdistdir}/fonts/afm/public/bera
%exclude %{texmfdistdir}/fonts/map/dvips/bera
%exclude %{texmfdistdir}/fonts/tfm/public/bera
%exclude %{texmfdistdir}/fonts/type1/public/bera
%exclude %{texmfdistdir}/fonts/vf/public/bera
%exclude %{texmfdistdir}/tex/latex/bera
# blacklettert1
%exclude %{texmfdistdir}/fonts/tfm/public/blacklettert1
%exclude %{texmfdistdir}/fonts/vf/public/blacklettert1
%exclude %{texmfdistdir}/tex/latex/blacklettert1
# boisik
%exclude %{texmfdistdir}/fonts/source/public/boisik
%exclude %{texmfdistdir}/fonts/tfm/public/boisik
%exclude %{texmfdistdir}/tex/latex/boisik
# bookhands
%exclude %{texmfdistdir}/fonts/afm/public/bookhands
%exclude %{texmfdistdir}/fonts/map/dvips/bookhands
%exclude %{texmfdistdir}/fonts/source/public/bookhands
%exclude %{texmfdistdir}/fonts/tfm/public/bookhands
%exclude %{texmfdistdir}/fonts/type1/public/bookhands
%exclude %{texmfdistdir}/tex/latex/bookhands
# boondox
%exclude %{texmfdistdir}/fonts/map/dvips/boondox
%exclude %{texmfdistdir}/fonts/tfm/public/boondox
%exclude %{texmfdistdir}/fonts/type1/public/boondox
%exclude %{texmfdistdir}/fonts/vf/public/boondox
%exclude %{texmfdistdir}/tex/latex/boondox
# braille
%exclude %{texmfdistdir}/tex/latex/braille
# brushscr
%exclude %{texmfdistdir}/dvips/brushscr
%exclude %{texmfdistdir}/fonts/afm/public/brushscr
%exclude %{texmfdistdir}/fonts/map/dvips/brushscr
%exclude %{texmfdistdir}/fonts/tfm/public/brushscr
%exclude %{texmfdistdir}/fonts/type1/public/brushscr
%exclude %{texmfdistdir}/fonts/vf/public/brushscr
%exclude %{texmfdistdir}/tex/latex/brushscr
# calligra
%exclude %{texmfdistdir}/fonts/source/public/calligra
%exclude %{texmfdistdir}/fonts/tfm/public/calligra
# cantarell
%exclude %{texmfdistdir}/fonts/afm/public/cantarell
%exclude %{texmfdistdir}/fonts/enc/dvips/cantarell
%exclude %{texmfdistdir}/fonts/map/dvips/cantarell
%exclude %{texmfdistdir}/fonts/tfm/public/cantarell
%exclude %{texmfdistdir}/fonts/type1/public/cantarell
%exclude %{texmfdistdir}/fonts/vf/public/cantarell
%exclude %{texmfdistdir}/tex/latex/cantarell
# carolmin-ps
%exclude %{texmfdistdir}/fonts/afm/public/carolmin-ps
%exclude %{texmfdistdir}/fonts/map/dvips/carolmin-ps
%exclude %{texmfdistdir}/fonts/type1/public/carolmin-ps
# ccicons
%exclude %{texmfdistdir}/fonts/afm/public/ccicons
%exclude %{texmfdistdir}/fonts/enc/dvips/ccicons
%exclude %{texmfdistdir}/fonts/map/dvips/ccicons
%exclude %{texmfdistdir}/fonts/tfm/public/ccicons
%exclude %{texmfdistdir}/fonts/type1/public/ccicons
%exclude %{texmfdistdir}/tex/latex/ccicons
# cfr-lm
%exclude %{texmfdistdir}/fonts/enc/dvips/cfr-lm
%exclude %{texmfdistdir}/fonts/map/dvips/cfr-lm
%exclude %{texmfdistdir}/fonts/tfm/public/cfr-lm
%exclude %{texmfdistdir}/fonts/vf/public/cfr-lm
%exclude %{texmfdistdir}/tex/latex/cfr-lm
# cherokee
%exclude %{texmfdistdir}/fonts/source/public/cherokee
%exclude %{texmfdistdir}/fonts/tfm/public/cherokee
%exclude %{texmfdistdir}/tex/latex/cherokee
# cm-lgc
%exclude %{texmfdistdir}/fonts/afm/public/cm-lgc
%exclude %{texmfdistdir}/fonts/enc/dvips/cm-lgc
%exclude %{texmfdistdir}/fonts/map/dvips/cm-lgc
%exclude %{texmfdistdir}/fonts/ofm/public/cm-lgc
%exclude %{texmfdistdir}/fonts/ovf/public/cm-lgc
%exclude %{texmfdistdir}/fonts/tfm/public/cm-lgc
%exclude %{texmfdistdir}/fonts/type1/public/cm-lgc
%exclude %{texmfdistdir}/fonts/vf/public/cm-lgc
%exclude %{texmfdistdir}/tex/latex/cm-lgc
# cm-unicode
%exclude %{texmfdistdir}/fonts/afm/public/cm-unicode
%exclude %{texmfdistdir}/fonts/enc/dvips/cm-unicode
%exclude %{texmfdistdir}/fonts/map/dvips/cm-unicode
%exclude %{texmfdistdir}/fonts/opentype/public/cm-unicode
%exclude %{texmfdistdir}/fonts/type1/public/cm-unicode
# cmbright
%exclude %{texmfdistdir}/fonts/source/public/cmbright
%exclude %{texmfdistdir}/fonts/tfm/public/cmbright
%exclude %{texmfdistdir}/tex/latex/cmbright
# cmll
%exclude %{texmfdistdir}/fonts/map/dvips/cmll
%exclude %{texmfdistdir}/fonts/source/public/cmll
%exclude %{texmfdistdir}/fonts/tfm/public/cmll
%exclude %{texmfdistdir}/fonts/type1/public/cmll
%exclude %{texmfdistdir}/tex/latex/cmll
# cmpica
%exclude %{texmfdistdir}/fonts/source/public/cmpica
%exclude %{texmfdistdir}/fonts/tfm/public/cmpica
# collection-basic
%exclude %{texmfdistdir}/tex/latex/collref
# concmath-fonts
%exclude %{texmfdistdir}/fonts/source/public/concmath-fonts
%exclude %{texmfdistdir}/fonts/tfm/public/concmath-fonts
# courier-scaled
%exclude %{texmfdistdir}/tex/latex/courier-scaled
# cryst
%exclude %{texmfdistdir}/fonts/afm/public/cryst
%exclude %{texmfdistdir}/fonts/source/public/cryst
%exclude %{texmfdistdir}/fonts/tfm/public/cryst
%exclude %{texmfdistdir}/fonts/type1/public/cryst
# cyklop
%exclude %{texmfdistdir}/fonts/afm/public/cyklop
%exclude %{texmfdistdir}/fonts/enc/dvips/cyklop
%exclude %{texmfdistdir}/fonts/map/dvips/cyklop
%exclude %{texmfdistdir}/fonts/opentype/public/cyklop
%exclude %{texmfdistdir}/fonts/tfm/public/cyklop
%exclude %{texmfdistdir}/fonts/type1/public/cyklop
%exclude %{texmfdistdir}/tex/latex/cyklop
# dancers
%exclude %{texmfdistdir}/fonts/source/public/dancers
%exclude %{texmfdistdir}/fonts/tfm/public/dancers
# dice
%exclude %{texmfdistdir}/fonts/source/public/dice
%exclude %{texmfdistdir}/fonts/tfm/public/dice
# dictsym
%exclude %{texmfdistdir}/fonts/afm/public/dictsym
%exclude %{texmfdistdir}/fonts/map/dvips/dictsym
%exclude %{texmfdistdir}/fonts/tfm/public/dictsym
%exclude %{texmfdistdir}/fonts/type1/public/dictsym
%exclude %{texmfdistdir}/tex/latex/dictsym
# dingbat
%exclude %{texmfdistdir}/fonts/source/public/dingbat
%exclude %{texmfdistdir}/fonts/tfm/public/dingbat
%exclude %{texmfdistdir}/tex/latex/dingbat
# doublestroke
%exclude %{texmfdistdir}/fonts/map/dvips/doublestroke
%exclude %{texmfdistdir}/fonts/source/public/doublestroke
%exclude %{texmfdistdir}/fonts/tfm/public/doublestroke
%exclude %{texmfdistdir}/fonts/type1/public/doublestroke
%exclude %{texmfdistdir}/tex/latex/doublestroke
# dozenal
%exclude %{texmfdistdir}/fonts/map/dvips/dozenal
%exclude %{texmfdistdir}/fonts/source/public/dozenal
%exclude %{texmfdistdir}/fonts/tfm/public/dozenal
%exclude %{texmfdistdir}/fonts/type1/public/dozenal
%exclude %{texmfdistdir}/fonts/vf/public/dozenal
%exclude %{texmfdistdir}/tex/latex/dozenal
# duerer
%exclude %{texmfdistdir}/fonts/source/public/duerer
%exclude %{texmfdistdir}/fonts/tfm/public/duerer
# duerer-latex
%exclude %{texmfdistdir}/tex/latex/duerer-latex
# ean
%exclude %{texmfdistdir}/tex/generic/ean
# ecc
%exclude %{texmfdistdir}/fonts/source/public/ecc
%exclude %{texmfdistdir}/fonts/tfm/public/ecc
# eco
%exclude %{texmfdistdir}/fonts/tfm/public/eco
%exclude %{texmfdistdir}/fonts/vf/public/eco
%exclude %{texmfdistdir}/tex/latex/eco
# eiad
%exclude %{texmfdistdir}/fonts/source/public/eiad
%exclude %{texmfdistdir}/fonts/tfm/public/eiad
%exclude %{texmfdistdir}/tex/latex/eiad
# eiad-ltx
%exclude %{texmfdistdir}/fonts/source/public/eiad-ltx
%exclude %{texmfdistdir}/tex/latex/eiad-ltx
# elvish
%exclude %{texmfdistdir}/fonts/source/public/elvish
%exclude %{texmfdistdir}/fonts/tfm/public/elvish
# epigrafica
%exclude %{texmfdistdir}/fonts/afm/public/epigrafica
%exclude %{texmfdistdir}/fonts/enc/dvips/epigrafica
%exclude %{texmfdistdir}/fonts/map/dvips/epigrafica
%exclude %{texmfdistdir}/fonts/tfm/public/epigrafica
%exclude %{texmfdistdir}/fonts/type1/public/epigrafica
%exclude %{texmfdistdir}/fonts/vf/public/epigrafica
%exclude %{texmfdistdir}/tex/latex/epigrafica
# epsdice
%exclude %{texmfdistdir}/tex/latex/epsdice
# esstix
%exclude %{texmfdistdir}/fonts/afm/esstix
%exclude %{texmfdistdir}/fonts/map/dvips/esstix
%exclude %{texmfdistdir}/fonts/tfm/public/esstix
%exclude %{texmfdistdir}/fonts/type1/public/esstix
%exclude %{texmfdistdir}/fonts/vf/public/esstix
%exclude %{texmfdistdir}/tex/latex/esstix
# esvect
%exclude %{texmfdistdir}/fonts/map/dvips/esvect
%exclude %{texmfdistdir}/fonts/source/public/esvect
%exclude %{texmfdistdir}/fonts/tfm/public/esvect
%exclude %{texmfdistdir}/fonts/type1/public/esvect
%exclude %{texmfdistdir}/tex/latex/esvect
# eulervm
%exclude %{texmfdistdir}/fonts/tfm/public/eulervm
%exclude %{texmfdistdir}/fonts/vf/public/eulervm
%exclude %{texmfdistdir}/tex/latex/eulervm
# euxm
%exclude %{texmfdistdir}/fonts/source/public/euxm
%exclude %{texmfdistdir}/fonts/tfm/public/euxm
# fdsymbol
%exclude %{texmfdistdir}/fonts/enc/dvips/fdsymbol
%exclude %{texmfdistdir}/fonts/map/dvips/fdsymbol
%exclude %{texmfdistdir}/fonts/source/public/fdsymbol
%exclude %{texmfdistdir}/fonts/tfm/public/fdsymbol
%exclude %{texmfdistdir}/fonts/type1/public/fdsymbol
%exclude %{texmfdistdir}/tex/latex/fdsymbol
# feyn
%exclude %{texmfdistdir}/fonts/source/public/feyn
%exclude %{texmfdistdir}/fonts/tfm/public/feyn
%exclude %{texmfdistdir}/tex/latex/feyn
# fge
%exclude %{texmfdistdir}/fonts/map/dvips/fge
%exclude %{texmfdistdir}/fonts/source/public/fge
%exclude %{texmfdistdir}/fonts/tfm/public/fge
%exclude %{texmfdistdir}/fonts/type1/public/fge
%exclude %{texmfdistdir}/tex/latex/fge
# foekfont
%exclude %{texmfdistdir}/fonts/map/dvips/foekfont
%exclude %{texmfdistdir}/fonts/tfm/public/foekfont
%exclude %{texmfdistdir}/fonts/type1/public/foekfont
%exclude %{texmfdistdir}/tex/latex/foekfont
# fonetika
%exclude %{texmfdistdir}/fonts/afm/public/fonetika
%exclude %{texmfdistdir}/fonts/map/dvips/fonetika
%exclude %{texmfdistdir}/fonts/tfm/public/fonetika
%exclude %{texmfdistdir}/fonts/truetype/public/fonetika
%exclude %{texmfdistdir}/fonts/type1/public/fonetika
%exclude %{texmfdistdir}/tex/latex/fonetika
# fourier
%exclude %{texmfdistdir}/fonts/afm/public/fourier
%exclude %{texmfdistdir}/fonts/map/dvips/fourier
%exclude %{texmfdistdir}/fonts/tfm/public/fourier
%exclude %{texmfdistdir}/fonts/type1/public/fourier
%exclude %{texmfdistdir}/fonts/vf/public/fourier
%exclude %{texmfdistdir}/tex/latex/fourier
# fouriernc
%exclude %{texmfdistdir}/fonts/afm/public/fouriernc
%exclude %{texmfdistdir}/fonts/tfm/public/fouriernc
%exclude %{texmfdistdir}/fonts/vf/public/fouriernc
%exclude %{texmfdistdir}/tex/latex/fouriernc
# frcursive
%exclude %{texmfdistdir}/fonts/source/public/frcursive
%exclude %{texmfdistdir}/fonts/tfm/public/frcursive
%exclude %{texmfdistdir}/metapost/frcursive
%exclude %{texmfdistdir}/tex/latex/frcursive
# genealogy
%exclude %{texmfdistdir}/fonts/source/public/genealogy
%exclude %{texmfdistdir}/fonts/tfm/public/genealogy
# gentium
%exclude %{texmfdistdir}/fonts/afm/public/gentium
%exclude %{texmfdistdir}/fonts/enc/dvips/gentium
%exclude %{texmfdistdir}/fonts/map/pdftex/gentium
%exclude %{texmfdistdir}/fonts/tfm/public/gentium
%exclude %{texmfdistdir}/fonts/truetype/public/gentium
%exclude %{texmfdistdir}/tex/context/third/gentium
# gfsartemisia
%exclude %{texmfdistdir}/fonts/afm/public/gfsartemisia
%exclude %{texmfdistdir}/fonts/enc/dvips/gfsartemisia
%exclude %{texmfdistdir}/fonts/map/dvips/gfsartemisia
%exclude %{texmfdistdir}/fonts/opentype/public/gfsartemisia
%exclude %{texmfdistdir}/fonts/tfm/public/gfsartemisia
%exclude %{texmfdistdir}/fonts/type1/public/gfsartemisia
%exclude %{texmfdistdir}/fonts/vf/public/gfsartemisia
%exclude %{texmfdistdir}/tex/latex/gfsartemisia
# gfsbodoni
%exclude %{texmfdistdir}/fonts/afm/public/gfsbodoni
%exclude %{texmfdistdir}/fonts/enc/dvips/gfsbodoni
%exclude %{texmfdistdir}/fonts/map/dvips/gfsbodoni
%exclude %{texmfdistdir}/fonts/opentype/public/gfsbodoni
%exclude %{texmfdistdir}/fonts/tfm/public/gfsbodoni
%exclude %{texmfdistdir}/fonts/type1/public/gfsbodoni
%exclude %{texmfdistdir}/fonts/vf/public/gfsbodoni
%exclude %{texmfdistdir}/tex/latex/gfsbodoni
# gfscomplutum
%exclude %{texmfdistdir}/fonts/afm/public/gfscomplutum
%exclude %{texmfdistdir}/fonts/enc/dvips/gfscomplutum
%exclude %{texmfdistdir}/fonts/map/dvips/gfscomplutum
%exclude %{texmfdistdir}/fonts/opentype/public/gfscomplutum
%exclude %{texmfdistdir}/fonts/tfm/public/gfscomplutum
%exclude %{texmfdistdir}/fonts/type1/public/gfscomplutum
%exclude %{texmfdistdir}/fonts/vf/public/gfscomplutum
%exclude %{texmfdistdir}/tex/latex/gfscomplutum
# gfsdidot
%exclude %{texmfdistdir}/fonts/afm/public/gfsdidot
%exclude %{texmfdistdir}/fonts/enc/dvips/gfsdidot
%exclude %{texmfdistdir}/fonts/map/dvips/gfsdidot
%exclude %{texmfdistdir}/fonts/opentype/public/gfsdidot
%exclude %{texmfdistdir}/fonts/tfm/public/gfsdidot
%exclude %{texmfdistdir}/fonts/type1/public/gfsdidot
%exclude %{texmfdistdir}/fonts/vf/public/gfsdidot
%exclude %{texmfdistdir}/tex/latex/gfsdidot
# gfsneohellenic
%exclude %{texmfdistdir}/fonts/afm/public/gfsneohellenic
%exclude %{texmfdistdir}/fonts/enc/dvips/gfsneohellenic
%exclude %{texmfdistdir}/fonts/map/dvips/gfsneohellenic
%exclude %{texmfdistdir}/fonts/opentype/public/gfsneohellenic
%exclude %{texmfdistdir}/fonts/tfm/public/gfsneohellenic
%exclude %{texmfdistdir}/fonts/type1/public/gfsneohellenic
%exclude %{texmfdistdir}/fonts/vf/public/gfsneohellenic
%exclude %{texmfdistdir}/tex/latex/gfsneohellenic
# gfssolomos
%exclude %{texmfdistdir}/fonts/afm/public/gfssolomos
%exclude %{texmfdistdir}/fonts/enc/dvips/gfssolomos
%exclude %{texmfdistdir}/fonts/map/dvips/gfssolomos
%exclude %{texmfdistdir}/fonts/opentype/public/gfssolomos
%exclude %{texmfdistdir}/fonts/tfm/public/gfssolomos
%exclude %{texmfdistdir}/fonts/type1/public/gfssolomos
%exclude %{texmfdistdir}/fonts/vf/public/gfssolomos
%exclude %{texmfdistdir}/tex/latex/gfssolomos
# gnu-freefont
%exclude %{texmfdistdir}/fonts/opentype/public/gnu-freefont
%exclude %{texmfdistdir}/fonts/truetype/public/gnu-freefont
# greenpoint
%exclude %{texmfdistdir}/fonts/source/public/greenpoint
%exclude %{texmfdistdir}/fonts/tfm/public/greenpoint
# grotesq
%exclude %{texmfdistdir}/dvips/grotesq
%exclude %{texmfdistdir}/fonts/afm/urw/grotesq
%exclude %{texmfdistdir}/fonts/map/dvips/grotesq
%exclude %{texmfdistdir}/fonts/tfm/urw/grotesq
%exclude %{texmfdistdir}/fonts/type1/urw/grotesq
%exclude %{texmfdistdir}/fonts/vf/urw/grotesq
%exclude %{texmfdistdir}/tex/latex/grotesq
# hands
%exclude %{texmfdistdir}/fonts/source/public/hands
%exclude %{texmfdistdir}/fonts/tfm/public/hands
# hfbright
%exclude %{texmfdistdir}/dvips/hfbright
%exclude %{texmfdistdir}/fonts/afm/public/hfbright
%exclude %{texmfdistdir}/fonts/enc/dvips/hfbright
%exclude %{texmfdistdir}/fonts/map/dvips/hfbright
%exclude %{texmfdistdir}/fonts/type1/public/hfbright
# hfoldsty
%exclude %{texmfdistdir}/fonts/tfm/public/hfoldsty
%exclude %{texmfdistdir}/fonts/vf/public/hfoldsty
%exclude %{texmfdistdir}/tex/latex/hfoldsty
# ifsym
%exclude %{texmfdistdir}/fonts/source/public/ifsym
%exclude %{texmfdistdir}/fonts/tfm/public/ifsym
%exclude %{texmfdistdir}/tex/latex/ifsym
# inconsolata
%exclude %{texmfdistdir}/fonts/enc/dvips/inconsolata
%exclude %{texmfdistdir}/fonts/map/dvips/inconsolata
%exclude %{texmfdistdir}/fonts/opentype/public/inconsolata
%exclude %{texmfdistdir}/fonts/tfm/public/inconsolata
%exclude %{texmfdistdir}/fonts/type1/public/inconsolata
%exclude %{texmfdistdir}/tex/latex/inconsolata
# initials
%exclude %{texmfdistdir}/dvips/initials
%exclude %{texmfdistdir}/fonts/afm/public/initials
%exclude %{texmfdistdir}/fonts/map/dvips/initials
%exclude %{texmfdistdir}/fonts/tfm/public/initials
%exclude %{texmfdistdir}/fonts/type1/public/initials
%exclude %{texmfdistdir}/tex/latex/initials
# jablantile
%exclude %{texmfdistdir}/fonts/source/public/jablantile
# junicode
%exclude %{texmfdistdir}/fonts/truetype/public/junicode
# kixfont
%exclude %{texmfdistdir}/fonts/source/public/kixfont
%exclude %{texmfdistdir}/fonts/tfm/public/kixfont
# knuthotherfonts
%exclude %{texmfdistdir}/fonts/source/public/knuthotherfonts/committee
%exclude %{texmfdistdir}/fonts/source/public/knuthotherfonts/halftone
%exclude %{texmfdistdir}/fonts/source/public/knuthotherfonts/mfbook
# kpfonts
%exclude %{texmfdistdir}/fonts/afm/public/kpfonts
%exclude %{texmfdistdir}/fonts/enc/dvips/kpfonts
%exclude %{texmfdistdir}/fonts/enc/pdftex/kpfonts
%exclude %{texmfdistdir}/fonts/map/dvips/kpfonts
%exclude %{texmfdistdir}/fonts/source/public/kpfonts
%exclude %{texmfdistdir}/fonts/tfm/public/kpfonts
%exclude %{texmfdistdir}/fonts/type1/public/kpfonts
%exclude %{texmfdistdir}/fonts/vf/public/kpfonts
%exclude %{texmfdistdir}/tex/latex/kpfonts
# lfb
%exclude %{texmfdistdir}/fonts/source/public/lfb
%exclude %{texmfdistdir}/fonts/tfm/public/lfb
# libertine
%exclude %{texmfdistdir}/dvips/libertine
%exclude %{texmfdistdir}/fonts/afm/public/libertine
%exclude %{texmfdistdir}/fonts/enc/dvips/libertine
%exclude %{texmfdistdir}/fonts/map/dvips/libertine
%exclude %{texmfdistdir}/fonts/opentype/public/libertine
%exclude %{texmfdistdir}/fonts/tfm/public/libertine
%exclude %{texmfdistdir}/fonts/type1/public/libertine
%exclude %{texmfdistdir}/fonts/vf/public/libertine
%exclude %{texmfdistdir}/tex/latex/libertine
# libris
%exclude %{texmfdistdir}/fonts/afm/arkandis/libris
%exclude %{texmfdistdir}/fonts/enc/dvips/libris
%exclude %{texmfdistdir}/fonts/map/dvips/libris
%exclude %{texmfdistdir}/fonts/tfm/arkandis/libris
%exclude %{texmfdistdir}/fonts/type1/arkandis/libris
%exclude %{texmfdistdir}/fonts/vf/arkandis/libris
%exclude %{texmfdistdir}/tex/latex/libris
# linearA
%exclude %{texmfdistdir}/fonts/afm/public/linearA
%exclude %{texmfdistdir}/fonts/map/dvips/linearA
%exclude %{texmfdistdir}/fonts/tfm/public/linearA
%exclude %{texmfdistdir}/fonts/type1/public/linearA
%exclude %{texmfdistdir}/tex/latex/linearA
# lxfonts
%exclude %{texmfdistdir}/fonts/map/dvips/lxfonts
%exclude %{texmfdistdir}/fonts/source/public/lxfonts
%exclude %{texmfdistdir}/fonts/tfm/public/lxfonts
%exclude %{texmfdistdir}/fonts/type1/public/lxfonts
%exclude %{texmfdistdir}/tex/latex/lxfonts
# ly1
%exclude %{texmfdistdir}/fonts/enc/dvips/ly1
%exclude %{texmfdistdir}/fonts/map/dvips/ly1
%exclude %{texmfdistdir}/fonts/tfm/adobe/ly1
%exclude %{texmfdistdir}/fonts/vf/adobe/ly1
%exclude %{texmfdistdir}/tex/latex/ly1
%exclude %{texmfdistdir}/tex/plain/ly1
# mathabx
%exclude %{texmfdistdir}/fonts/source/public/mathabx
%exclude %{texmfdistdir}/fonts/tfm/public/mathabx
%exclude %{texmfdistdir}/tex/generic/mathabx
# mathdesign
%exclude %{texmfdistdir}/dvips/mathdesign
%exclude %{texmfdistdir}/fonts/afm/mathdesign/mdbch
%exclude %{texmfdistdir}/fonts/afm/mathdesign/mdput
%exclude %{texmfdistdir}/fonts/afm/mathdesign/mdugm
%exclude %{texmfdistdir}/fonts/map/dvips/mathdesign
%exclude %{texmfdistdir}/fonts/tfm/mathdesign/mdbch
%exclude %{texmfdistdir}/fonts/tfm/mathdesign/mdput
%exclude %{texmfdistdir}/fonts/tfm/mathdesign/mdugm
%exclude %{texmfdistdir}/fonts/type1/mathdesign/mdbch
%exclude %{texmfdistdir}/fonts/type1/mathdesign/mdput
%exclude %{texmfdistdir}/fonts/type1/mathdesign/mdugm
%exclude %{texmfdistdir}/fonts/vf/mathdesign/mdbch
%exclude %{texmfdistdir}/fonts/vf/mathdesign/mdput
%exclude %{texmfdistdir}/fonts/vf/mathdesign/mdugm
%exclude %{texmfdistdir}/tex/latex/mathdesign
# mnsymbol
%exclude %{texmfdistdir}/fonts/enc/dvips/mnsymbol
%exclude %{texmfdistdir}/fonts/map/dvips/mnsymbol
%exclude %{texmfdistdir}/fonts/map/vtex/mnsymbol
%exclude %{texmfdistdir}/fonts/opentype/public/mnsymbol
%exclude %{texmfdistdir}/fonts/source/public/mnsymbol
%exclude %{texmfdistdir}/fonts/tfm/public/mnsymbol
%exclude %{texmfdistdir}/fonts/type1/public/mnsymbol
%exclude %{texmfdistdir}/tex/latex/mnsymbol
# nkarta
%exclude %{texmfdistdir}/fonts/source/public/nkarta
%exclude %{texmfdistdir}/fonts/tfm/public/nkarta
%exclude %{texmfdistdir}/metapost/nkarta
# ocherokee
%exclude %{texmfdistdir}/fonts/afm/public/ocherokee
%exclude %{texmfdistdir}/fonts/map/dvips/ocherokee
%exclude %{texmfdistdir}/fonts/ofm/public/ocherokee
%exclude %{texmfdistdir}/fonts/ovf/public/ocherokee
%exclude %{texmfdistdir}/fonts/ovp/public/ocherokee
%exclude %{texmfdistdir}/fonts/tfm/public/ocherokee
%exclude %{texmfdistdir}/fonts/type1/public/ocherokee
%exclude %{texmfdistdir}/omega/ocp/ocherokee
%exclude %{texmfdistdir}/omega/otp/ocherokee
# ogham
%exclude %{texmfdistdir}/fonts/source/public/ogham
%exclude %{texmfdistdir}/fonts/tfm/public/ogham
# oinuit
%exclude %{texmfdistdir}/fonts/map/dvips/oinuit
%exclude %{texmfdistdir}/fonts/ofm/public/oinuit
%exclude %{texmfdistdir}/fonts/ovf/public/oinuit
%exclude %{texmfdistdir}/fonts/tfm/public/oinuit
%exclude %{texmfdistdir}/fonts/type1/public/oinuit
%exclude %{texmfdistdir}/omega/ocp/oinuit
%exclude %{texmfdistdir}/tex/lambda/oinuit
# oldlatin
%exclude %{texmfdistdir}/fonts/source/public/oldlatin
%exclude %{texmfdistdir}/fonts/tfm/public/oldlatin
# oldstandard
%exclude %{texmfdistdir}/fonts/opentype/public/oldstandard
# orkhun
%exclude %{texmfdistdir}/fonts/source/public/orkhun
%exclude %{texmfdistdir}/fonts/tfm/public/orkhun
# pacioli
%exclude %{texmfdistdir}/fonts/source/public/pacioli
%exclude %{texmfdistdir}/fonts/tfm/public/pacioli
%exclude %{texmfdistdir}/tex/latex/pacioli
# phaistos
%exclude %{texmfdistdir}/fonts/afm/public/phaistos
%exclude %{texmfdistdir}/fonts/map/dvips/phaistos
%exclude %{texmfdistdir}/fonts/opentype/public/phaistos
%exclude %{texmfdistdir}/fonts/tfm/public/phaistos
%exclude %{texmfdistdir}/fonts/type1/public/phaistos
%exclude %{texmfdistdir}/tex/latex/phaistos
# phonetic
%exclude %{texmfdistdir}/fonts/source/public/phonetic
%exclude %{texmfdistdir}/fonts/tfm/public/phonetic
%exclude %{texmfdistdir}/tex/latex/phonetic
# pigpen
%exclude %{texmfdistdir}/fonts/map/dvips/pigpen
%exclude %{texmfdistdir}/fonts/source/public/pigpen
%exclude %{texmfdistdir}/fonts/tfm/public/pigpen
%exclude %{texmfdistdir}/fonts/type1/public/pigpen
%exclude %{texmfdistdir}/tex/latex/pigpen
# prodint
%exclude %{texmfdistdir}/fonts/afm/public/prodint
%exclude %{texmfdistdir}/fonts/map/dvips/prodint
%exclude %{texmfdistdir}/fonts/tfm/public/prodint
%exclude %{texmfdistdir}/fonts/type1/public/prodint
%exclude %{texmfdistdir}/tex/latex/prodint
# psafm
%exclude %{texmfdistdir}/fonts/afm/itc/psafm/stonesan
# punk
%exclude %{texmfdistdir}/fonts/source/public/punk
%exclude %{texmfdistdir}/fonts/tfm/public/punk
# recycle
%exclude %{texmfdistdir}/fonts/map/dvips/recycle
%exclude %{texmfdistdir}/fonts/source/public/recycle
%exclude %{texmfdistdir}/fonts/tfm/public/recycle
%exclude %{texmfdistdir}/fonts/type1/public/recycle
%exclude %{texmfdistdir}/tex/latex/recycle
# romande
%exclude %{texmfdistdir}/fonts/afm/arkandis/romande
%exclude %{texmfdistdir}/fonts/enc/dvips/romande
%exclude %{texmfdistdir}/fonts/map/dvips/romande
%exclude %{texmfdistdir}/fonts/tfm/arkandis/romande
%exclude %{texmfdistdir}/fonts/type1/arkandis/romande
%exclude %{texmfdistdir}/fonts/vf/arkandis/romande
%exclude %{texmfdistdir}/tex/latex/romande
# rsfso
%exclude %{texmfdistdir}/fonts/map/dvips/rsfso
%exclude %{texmfdistdir}/fonts/tfm/public/rsfso
%exclude %{texmfdistdir}/fonts/vf/public/rsfso
%exclude %{texmfdistdir}/tex/latex/public/rsfso
# sauter
%exclude %{texmfdistdir}/fonts/source/public/sauter
# sauterfonts
%exclude %{texmfdistdir}/tex/latex/sauterfonts
# semaphor
%exclude %{texmfdistdir}/fonts/afm/public/semaphor
%exclude %{texmfdistdir}/fonts/enc/dvips/semaphor
%exclude %{texmfdistdir}/fonts/map/dvips/semaphor
%exclude %{texmfdistdir}/fonts/opentype/public/semaphor
%exclude %{texmfdistdir}/fonts/source/public/semaphor
%exclude %{texmfdistdir}/fonts/tfm/public/semaphor
%exclude %{texmfdistdir}/fonts/type1/public/semaphor
%exclude %{texmfdistdir}/tex/context/third/semaphor
%exclude %{texmfdistdir}/tex/latex/semaphor
%exclude %{texmfdistdir}/tex/plain/semaphor
# skull
%exclude %{texmfdistdir}/fonts/source/public/skull
%exclude %{texmfdistdir}/tex/latex/skull
# staves
%exclude %{texmfdistdir}/fonts/map/dvips/staves
%exclude %{texmfdistdir}/fonts/tfm/public/staves
%exclude %{texmfdistdir}/fonts/type1/public/staves
%exclude %{texmfdistdir}/tex/latex/staves
# stix
%exclude %{texmfdistdir}/fonts/opentype/public/stix
# tapir
%exclude %{texmfdistdir}/fonts/source/public/tapir
%exclude %{texmfdistdir}/fonts/type1/public/tapir
# tengwarscript
%exclude %{texmfdistdir}/fonts/enc/dvips/tengwarscript
%exclude %{texmfdistdir}/fonts/map/dvips/tengwarscript
%exclude %{texmfdistdir}/fonts/tfm/public/tengwarscript
%exclude %{texmfdistdir}/fonts/vf/public/tengwarscript
%exclude %{texmfdistdir}/tex/latex/tengwarscript
# tpslifonts
%exclude %{texmfdistdir}/tex/latex/tpslifonts
# trajan
%exclude %{texmfdistdir}/fonts/afm/public/trajan
%exclude %{texmfdistdir}/fonts/map/dvips/trajan
%exclude %{texmfdistdir}/fonts/tfm/public/trajan
%exclude %{texmfdistdir}/fonts/type1/public/trajan
%exclude %{texmfdistdir}/tex/latex/trajan
# txfontsb
%exclude %{texmfdistdir}/fonts/afm/public/txfontsb
%exclude %{texmfdistdir}/fonts/enc/dvips/txfontsb
%exclude %{texmfdistdir}/fonts/map/dvips/txfontsb
%exclude %{texmfdistdir}/fonts/tfm/public/txfontsb
%exclude %{texmfdistdir}/fonts/type1/public/txfontsb
%exclude %{texmfdistdir}/fonts/vf/public/txfontsb
%exclude %{texmfdistdir}/tex/latex/txfontsb
# umtypewriter
%exclude %{texmfdistdir}/fonts/opentype/public/umtypewriter
# universa
%exclude %{texmfdistdir}/fonts/source/public/universa
%exclude %{texmfdistdir}/fonts/tfm/public/universa
%exclude %{texmfdistdir}/tex/latex/universa
# urwchancal
%exclude %{texmfdistdir}/fonts/tfm/urw/urwchancal
%exclude %{texmfdistdir}/fonts/vf/urw/urwchancal
%exclude %{texmfdistdir}/tex/latex/urwchancal
# venturisadf
%exclude %{texmfdistdir}/fonts/afm/arkandis/venturis
%exclude %{texmfdistdir}/fonts/afm/arkandis/venturis2
%exclude %{texmfdistdir}/fonts/afm/arkandis/venturisold
%exclude %{texmfdistdir}/fonts/afm/arkandis/venturissans
%exclude %{texmfdistdir}/fonts/afm/arkandis/venturissans2
%exclude %{texmfdistdir}/fonts/enc/dvips/venturisadf
%exclude %{texmfdistdir}/fonts/map/dvips/venturis
%exclude %{texmfdistdir}/fonts/map/dvips/venturis2
%exclude %{texmfdistdir}/fonts/map/dvips/venturisold
%exclude %{texmfdistdir}/fonts/map/dvips/venturissans
%exclude %{texmfdistdir}/fonts/map/dvips/venturissans2
%exclude %{texmfdistdir}/fonts/tfm/arkandis/venturis
%exclude %{texmfdistdir}/fonts/tfm/arkandis/venturis2
%exclude %{texmfdistdir}/fonts/tfm/arkandis/venturisold
%exclude %{texmfdistdir}/fonts/tfm/arkandis/venturissans
%exclude %{texmfdistdir}/fonts/tfm/arkandis/venturissans2
%exclude %{texmfdistdir}/fonts/type1/arkandis/venturis
%exclude %{texmfdistdir}/fonts/type1/arkandis/venturis2
%exclude %{texmfdistdir}/fonts/type1/arkandis/venturisold
%exclude %{texmfdistdir}/fonts/type1/arkandis/venturissans
%exclude %{texmfdistdir}/fonts/type1/arkandis/venturissans2
%exclude %{texmfdistdir}/fonts/vf/arkandis/venturis
%exclude %{texmfdistdir}/fonts/vf/arkandis/venturis2
%exclude %{texmfdistdir}/fonts/vf/arkandis/venturisold
%exclude %{texmfdistdir}/fonts/vf/arkandis/venturissans
%exclude %{texmfdistdir}/fonts/vf/arkandis/venturissans2
%exclude %{texmfdistdir}/tex/latex/venturis
%exclude %{texmfdistdir}/tex/latex/venturis2
%exclude %{texmfdistdir}/tex/latex/venturisadf
%exclude %{texmfdistdir}/tex/latex/venturisold
%exclude %{texmfdistdir}/tex/latex/venturissans
%exclude %{texmfdistdir}/tex/latex/venturissans2
# wsuipa
%exclude %{texmfdistdir}/fonts/source/public/wsuipa
%exclude %{texmfdistdir}/fonts/tfm/public/wsuipa
%exclude %{texmfdistdir}/tex/latex/wsuipa
# xits
%exclude %{texmfdistdir}/fonts/opentype/public/xits
# yfonts
%exclude %{texmfdistdir}/tex/latex/yfonts

%{texmfdistdir}/makeindex
%{texmfdistdir}/metafont
%{texmfdistdir}/metapost
%{texmfdistdir}/mft
%{texmfdistdir}/omega
%{texmfdistdir}/pbibtex
%{texmfdistdir}/scripts
%{texmfdistdir}/tex
%if !%{with_system_tex4ht}
%{texmfdistdir}/tex4ht
%if %mdkversion >= 201100
%{_javadir}/tex4ht.jar
%endif
%endif
%{texmfdistdir}/texdoc
%dir %{texmflocaldir}

%if %mdkversion >= 201100
%post
for info in	asy-faq asymptote dvipng dvips eplain epspdf fontname \
		kpathsea latex2e latex2man tds texdraw web2c; do
    /sbin/install-info %{_infodir}/${info}* %{_infodir}/dir ||:
done

%preun
if [ "$1" = "0" ];then
    for info in	asy-faq asymptote dvipng dvips eplain epspdf fontname \
		kpathsea latex2e latex2man tds texdraw web2c; do
	/sbin/install-info --remove %{_infodir}/${info}* %{_infodir}/dir ||:
    done
fi
%endif

#-----------------------------------------------------------------------
%package	-n texlive-doc
Summary:	Tex Live documentation
Group:		Publishing
%if %mdkversion <= 201200
Provides:	tetex-doc = %{version}
Provides:	texlive-texmf-doc = %{version}
%endif
Obsoletes:	tetex-doc <= 3.0
Obsoletes:	texlive-texmf-doc <= 2007
Requires:	texlive-texmf = %{version}-%{release}

%description	-n texlive-doc
TeX Live is an easy way to get up and running with the TeX document
production system. It provides a comprehensive TeX system. It includes
all the major TeX-related programs, macro packages, and fonts that are
free software, including support for many languages around the world.

%files		-n texlive-doc
%defattr(-,root,root,-)
%{texmfdir}/doc/*
%exclude %{texmfdir}/doc/tetex
%if %{enable_asymptote}
%exclude %{texmfdir}/doc/asymptote
%endif
%if %{enable_xindy}
%exclude %{texmfdir}/doc/xindy
%endif
%{texmfdistdir}/doc

#-----------------------------------------------------------------------
%package	-n texlive-fontsextra
Summary:	TeX Live extra fonts
Group:		Publishing
Requires(post):	texlive-texmf = %{version}-%{release}

%description	-n texlive-fontsextra
TeX Live is an easy way to get up and running with the TeX document
production system. It provides a comprehensive TeX system. It includes
all the major TeX-related programs, macro packages, and fonts that are
free software, including support for many languages around the world.

%files		-n texlive-fontsextra
%defattr(-,root,root,-)
# collection-fontsextra
# allrunes
%{texmfdistdir}/fonts/map/dvips/allrunes
%{texmfdistdir}/fonts/source/public/allrunes
%{texmfdistdir}/fonts/type1/public/allrunes
%{texmfdistdir}/tex/latex/allrunes
# antiqua
%{texmfdistdir}/dvips/antiqua
%{texmfdistdir}/fonts/afm/urw/antiqua
%{texmfdistdir}/fonts/map/dvips/antiqua
%{texmfdistdir}/fonts/tfm/urw/antiqua
%{texmfdistdir}/fonts/type1/urw/antiqua
%{texmfdistdir}/fonts/vf/urw/antiqua
%{texmfdistdir}/tex/latex/antiqua
# antt
%{texmfdistdir}/fonts/afm/public/antt
%{texmfdistdir}/fonts/enc/dvips/antt
%{texmfdistdir}/fonts/map/dvips/antt
%{texmfdistdir}/fonts/opentype/public/antt
%{texmfdistdir}/fonts/tfm/public/antt
%{texmfdistdir}/fonts/type1/public/antt
%{texmfdistdir}/tex/latex/antt
%{texmfdistdir}/tex/plain/antt
# ar
%{texmfdistdir}/fonts/source/public/ar
%{texmfdistdir}/fonts/tfm/public/ar
%{texmfdistdir}/tex/latex/ar
# archaic
%{texmfdistdir}/fonts/afm/public/archaic
%{texmfdistdir}/fonts/map/dvips/archaic
%{texmfdistdir}/fonts/source/public/archaic
%{texmfdistdir}/fonts/tfm/public/archaic
%{texmfdistdir}/fonts/type1/public/archaic
%{texmfdistdir}/tex/latex/archaic
# arev
%{texmfdistdir}/fonts/afm/public/arev
%{texmfdistdir}/fonts/enc/dvips/arev
%{texmfdistdir}/fonts/map/dvips/arev
%{texmfdistdir}/fonts/tfm/public/arev
%{texmfdistdir}/fonts/type1/public/arev
%{texmfdistdir}/fonts/vf/public/arev
%{texmfdistdir}/tex/latex/arev
# ascii
%{texmfdistdir}/fonts/map/dvips/ascii
%{texmfdistdir}/fonts/tfm/public/ascii
%{texmfdistdir}/fonts/type1/public/ascii
%{texmfdistdir}/tex/latex/ascii
# astro
%{texmfdistdir}/fonts/source/public/astro
%{texmfdistdir}/fonts/tfm/public/astro
# augie
%{texmfdistdir}/fonts/afm/public/augie
%{texmfdistdir}/fonts/map/dvips/augie
%{texmfdistdir}/fonts/tfm/public/augie
%{texmfdistdir}/fonts/type1/public/augie
%{texmfdistdir}/fonts/vf/public/augie
%{texmfdistdir}/tex/latex/augie
# auncial-new
%{texmfdistdir}/fonts/afm/public/auncial-new
%{texmfdistdir}/fonts/map/dvips/auncial-new
%{texmfdistdir}/fonts/tfm/public/auncial-new
%{texmfdistdir}/fonts/type1/public/auncial-new
%{texmfdistdir}/tex/latex/auncial-new
# aurical
%{texmfdistdir}/fonts/afm/public/aurical
%{texmfdistdir}/fonts/map/dvips/aurical
%{texmfdistdir}/fonts/source/public/aurical
%{texmfdistdir}/fonts/tfm/public/aurical
%{texmfdistdir}/fonts/type1/public/aurical
%{texmfdistdir}/tex/latex/aurical
# barcodes
%{texmfdistdir}/fonts/source/public/barcodes
%{texmfdistdir}/fonts/tfm/public/barcodes
%{texmfdistdir}/tex/latex/barcodes
# baskervald
%{texmfdistdir}/fonts/afm/arkandis/baskervald
%{texmfdistdir}/fonts/enc/dvips/baskervald
%{texmfdistdir}/fonts/map/dvips/baskervald
%{texmfdistdir}/fonts/tfm/arkandis/baskervald
%{texmfdistdir}/fonts/type1/arkandis/baskervald
%{texmfdistdir}/fonts/vf/arkandis/baskervald
%{texmfdistdir}/tex/latex/baskervald
# bbding
%{texmfdistdir}/fonts/source/public/bbding
%{texmfdistdir}/fonts/tfm/public/bbding
%{texmfdistdir}/tex/latex/bbding
# bbm
%{texmfdistdir}/fonts/source/public/bbm
%{texmfdistdir}/fonts/tfm/public/bbm
# bbm-macros
%{texmfdistdir}/tex/latex/bbm-macros
# bbold
%{texmfdistdir}/fonts/source/public/bbold
%{texmfdistdir}/fonts/tfm/public/bbold
%{texmfdistdir}/tex/latex/bbold
# belleek
%{texmfdistdir}/fonts/map/dvips/belleek
%{texmfdistdir}/fonts/truetype/public/belleek
%{texmfdistdir}/fonts/type1/public/belleek
# bera
%{texmfdistdir}/fonts/afm/public/bera
%{texmfdistdir}/fonts/map/dvips/bera
%{texmfdistdir}/fonts/tfm/public/bera
%{texmfdistdir}/fonts/type1/public/bera
%{texmfdistdir}/fonts/vf/public/bera
%{texmfdistdir}/tex/latex/bera
# blacklettert1
%{texmfdistdir}/fonts/tfm/public/blacklettert1
%{texmfdistdir}/fonts/vf/public/blacklettert1
%{texmfdistdir}/tex/latex/blacklettert1
# boisik
%{texmfdistdir}/fonts/source/public/boisik
%{texmfdistdir}/fonts/tfm/public/boisik
%{texmfdistdir}/tex/latex/boisik
# bookhands
%{texmfdistdir}/fonts/afm/public/bookhands
%{texmfdistdir}/fonts/map/dvips/bookhands
%{texmfdistdir}/fonts/source/public/bookhands
%{texmfdistdir}/fonts/tfm/public/bookhands
%{texmfdistdir}/fonts/type1/public/bookhands
%{texmfdistdir}/tex/latex/bookhands
# boondox
%{texmfdistdir}/fonts/map/dvips/boondox
%{texmfdistdir}/fonts/tfm/public/boondox
%{texmfdistdir}/fonts/type1/public/boondox
%{texmfdistdir}/fonts/vf/public/boondox
%{texmfdistdir}/tex/latex/boondox
# braille
%{texmfdistdir}/tex/latex/braille
# brushscr
%{texmfdistdir}/dvips/brushscr
%{texmfdistdir}/fonts/afm/public/brushscr
%{texmfdistdir}/fonts/map/dvips/brushscr
%{texmfdistdir}/fonts/tfm/public/brushscr
%{texmfdistdir}/fonts/type1/public/brushscr
%{texmfdistdir}/fonts/vf/public/brushscr
%{texmfdistdir}/tex/latex/brushscr
# calligra
%{texmfdistdir}/fonts/source/public/calligra
%{texmfdistdir}/fonts/tfm/public/calligra
# cantarell
%{texmfdistdir}/fonts/afm/public/cantarell
%{texmfdistdir}/fonts/enc/dvips/cantarell
%{texmfdistdir}/fonts/map/dvips/cantarell
%{texmfdistdir}/fonts/tfm/public/cantarell
%{texmfdistdir}/fonts/type1/public/cantarell
%{texmfdistdir}/fonts/vf/public/cantarell
%{texmfdistdir}/tex/latex/cantarell
# carolmin-ps
%{texmfdistdir}/fonts/afm/public/carolmin-ps
%{texmfdistdir}/fonts/map/dvips/carolmin-ps
%{texmfdistdir}/fonts/type1/public/carolmin-ps
# ccicons
%{texmfdistdir}/fonts/afm/public/ccicons
%{texmfdistdir}/fonts/enc/dvips/ccicons
%{texmfdistdir}/fonts/map/dvips/ccicons
%{texmfdistdir}/fonts/tfm/public/ccicons
%{texmfdistdir}/fonts/type1/public/ccicons
%{texmfdistdir}/tex/latex/ccicons
# cfr-lm
%{texmfdistdir}/fonts/enc/dvips/cfr-lm
%{texmfdistdir}/fonts/map/dvips/cfr-lm
%{texmfdistdir}/fonts/tfm/public/cfr-lm
%{texmfdistdir}/fonts/vf/public/cfr-lm
%{texmfdistdir}/tex/latex/cfr-lm
# cherokee
%{texmfdistdir}/fonts/source/public/cherokee
%{texmfdistdir}/fonts/tfm/public/cherokee
%{texmfdistdir}/tex/latex/cherokee
# cm-lgc
%{texmfdistdir}/fonts/afm/public/cm-lgc
%{texmfdistdir}/fonts/enc/dvips/cm-lgc
%{texmfdistdir}/fonts/map/dvips/cm-lgc
%{texmfdistdir}/fonts/ofm/public/cm-lgc
%{texmfdistdir}/fonts/ovf/public/cm-lgc
%{texmfdistdir}/fonts/tfm/public/cm-lgc
%{texmfdistdir}/fonts/type1/public/cm-lgc
%{texmfdistdir}/fonts/vf/public/cm-lgc
%{texmfdistdir}/tex/latex/cm-lgc
# cm-unicode
%{texmfdistdir}/fonts/afm/public/cm-unicode
%{texmfdistdir}/fonts/enc/dvips/cm-unicode
%{texmfdistdir}/fonts/map/dvips/cm-unicode
%{texmfdistdir}/fonts/opentype/public/cm-unicode
%{texmfdistdir}/fonts/type1/public/cm-unicode
# cmbright
%{texmfdistdir}/fonts/source/public/cmbright
%{texmfdistdir}/fonts/tfm/public/cmbright
%{texmfdistdir}/tex/latex/cmbright
# cmll
%{texmfdistdir}/fonts/map/dvips/cmll
%{texmfdistdir}/fonts/source/public/cmll
%{texmfdistdir}/fonts/tfm/public/cmll
%{texmfdistdir}/fonts/type1/public/cmll
%{texmfdistdir}/tex/latex/cmll
# cmpica
%{texmfdistdir}/fonts/source/public/cmpica
%{texmfdistdir}/fonts/tfm/public/cmpica
# collection-basic
%{texmfdistdir}/tex/latex/collref
# concmath-fonts
%{texmfdistdir}/fonts/source/public/concmath-fonts
%{texmfdistdir}/fonts/tfm/public/concmath-fonts
# courier-scaled
%{texmfdistdir}/tex/latex/courier-scaled
# cryst
%{texmfdistdir}/fonts/afm/public/cryst
%{texmfdistdir}/fonts/source/public/cryst
%{texmfdistdir}/fonts/tfm/public/cryst
%{texmfdistdir}/fonts/type1/public/cryst
# cyklop
%{texmfdistdir}/fonts/afm/public/cyklop
%{texmfdistdir}/fonts/enc/dvips/cyklop
%{texmfdistdir}/fonts/map/dvips/cyklop
%{texmfdistdir}/fonts/opentype/public/cyklop
%{texmfdistdir}/fonts/tfm/public/cyklop
%{texmfdistdir}/fonts/type1/public/cyklop
%{texmfdistdir}/tex/latex/cyklop
# dancers
%{texmfdistdir}/fonts/source/public/dancers
%{texmfdistdir}/fonts/tfm/public/dancers
# dice
%{texmfdistdir}/fonts/source/public/dice
%{texmfdistdir}/fonts/tfm/public/dice
# dictsym
%{texmfdistdir}/fonts/afm/public/dictsym
%{texmfdistdir}/fonts/map/dvips/dictsym
%{texmfdistdir}/fonts/tfm/public/dictsym
%{texmfdistdir}/fonts/type1/public/dictsym
%{texmfdistdir}/tex/latex/dictsym
# dingbat
%{texmfdistdir}/fonts/source/public/dingbat
%{texmfdistdir}/fonts/tfm/public/dingbat
%{texmfdistdir}/tex/latex/dingbat
# doublestroke
%{texmfdistdir}/fonts/map/dvips/doublestroke
%{texmfdistdir}/fonts/source/public/doublestroke
%{texmfdistdir}/fonts/tfm/public/doublestroke
%{texmfdistdir}/fonts/type1/public/doublestroke
%{texmfdistdir}/tex/latex/doublestroke
# dozenal
%{texmfdistdir}/fonts/map/dvips/dozenal
%{texmfdistdir}/fonts/source/public/dozenal
%{texmfdistdir}/fonts/tfm/public/dozenal
%{texmfdistdir}/fonts/type1/public/dozenal
%{texmfdistdir}/fonts/vf/public/dozenal
%{texmfdistdir}/tex/latex/dozenal
# duerer
%{texmfdistdir}/fonts/source/public/duerer
%{texmfdistdir}/fonts/tfm/public/duerer
# duerer-latex
%{texmfdistdir}/tex/latex/duerer-latex
# ean
%{texmfdistdir}/tex/generic/ean
# ecc
%{texmfdistdir}/fonts/source/public/ecc
%{texmfdistdir}/fonts/tfm/public/ecc
# eco
%{texmfdistdir}/fonts/tfm/public/eco
%{texmfdistdir}/fonts/vf/public/eco
%{texmfdistdir}/tex/latex/eco
# eiad
%{texmfdistdir}/fonts/source/public/eiad
%{texmfdistdir}/fonts/tfm/public/eiad
%{texmfdistdir}/tex/latex/eiad
# eiad-ltx
%{texmfdistdir}/fonts/source/public/eiad-ltx
%{texmfdistdir}/tex/latex/eiad-ltx
# elvish
%{texmfdistdir}/fonts/source/public/elvish
%{texmfdistdir}/fonts/tfm/public/elvish
# epigrafica
%{texmfdistdir}/fonts/afm/public/epigrafica
%{texmfdistdir}/fonts/enc/dvips/epigrafica
%{texmfdistdir}/fonts/map/dvips/epigrafica
%{texmfdistdir}/fonts/tfm/public/epigrafica
%{texmfdistdir}/fonts/type1/public/epigrafica
%{texmfdistdir}/fonts/vf/public/epigrafica
%{texmfdistdir}/tex/latex/epigrafica
# epsdice
%{texmfdistdir}/tex/latex/epsdice
# esstix
%{texmfdistdir}/fonts/afm/esstix
%{texmfdistdir}/fonts/map/dvips/esstix
%{texmfdistdir}/fonts/tfm/public/esstix
%{texmfdistdir}/fonts/type1/public/esstix
%{texmfdistdir}/fonts/vf/public/esstix
%{texmfdistdir}/tex/latex/esstix
# esvect
%{texmfdistdir}/fonts/map/dvips/esvect
%{texmfdistdir}/fonts/source/public/esvect
%{texmfdistdir}/fonts/tfm/public/esvect
%{texmfdistdir}/fonts/type1/public/esvect
%{texmfdistdir}/tex/latex/esvect
# eulervm
%{texmfdistdir}/fonts/tfm/public/eulervm
%{texmfdistdir}/fonts/vf/public/eulervm
%{texmfdistdir}/tex/latex/eulervm
# euxm
%{texmfdistdir}/fonts/source/public/euxm
%{texmfdistdir}/fonts/tfm/public/euxm
# fdsymbol
%{texmfdistdir}/fonts/enc/dvips/fdsymbol
%{texmfdistdir}/fonts/map/dvips/fdsymbol
%{texmfdistdir}/fonts/source/public/fdsymbol
%{texmfdistdir}/fonts/tfm/public/fdsymbol
%{texmfdistdir}/fonts/type1/public/fdsymbol
%{texmfdistdir}/tex/latex/fdsymbol
# feyn
%{texmfdistdir}/fonts/source/public/feyn
%{texmfdistdir}/fonts/tfm/public/feyn
%{texmfdistdir}/tex/latex/feyn
# fge
%{texmfdistdir}/fonts/map/dvips/fge
%{texmfdistdir}/fonts/source/public/fge
%{texmfdistdir}/fonts/tfm/public/fge
%{texmfdistdir}/fonts/type1/public/fge
%{texmfdistdir}/tex/latex/fge
# foekfont
%{texmfdistdir}/fonts/map/dvips/foekfont
%{texmfdistdir}/fonts/tfm/public/foekfont
%{texmfdistdir}/fonts/type1/public/foekfont
%{texmfdistdir}/tex/latex/foekfont
# fonetika
%{texmfdistdir}/fonts/afm/public/fonetika
%{texmfdistdir}/fonts/map/dvips/fonetika
%{texmfdistdir}/fonts/tfm/public/fonetika
%{texmfdistdir}/fonts/truetype/public/fonetika
%{texmfdistdir}/fonts/type1/public/fonetika
%{texmfdistdir}/tex/latex/fonetika
# fourier
%{texmfdistdir}/fonts/afm/public/fourier
%{texmfdistdir}/fonts/map/dvips/fourier
%{texmfdistdir}/fonts/tfm/public/fourier
%{texmfdistdir}/fonts/type1/public/fourier
%{texmfdistdir}/fonts/vf/public/fourier
%{texmfdistdir}/tex/latex/fourier
# fouriernc
%{texmfdistdir}/fonts/afm/public/fouriernc
%{texmfdistdir}/fonts/tfm/public/fouriernc
%{texmfdistdir}/fonts/vf/public/fouriernc
%{texmfdistdir}/tex/latex/fouriernc
# frcursive
%{texmfdistdir}/fonts/source/public/frcursive
%{texmfdistdir}/fonts/tfm/public/frcursive
%{texmfdistdir}/metapost/frcursive
%{texmfdistdir}/tex/latex/frcursive
# genealogy
%{texmfdistdir}/fonts/source/public/genealogy
%{texmfdistdir}/fonts/tfm/public/genealogy
# gentium
%{texmfdistdir}/fonts/afm/public/gentium
%{texmfdistdir}/fonts/enc/dvips/gentium
%{texmfdistdir}/fonts/map/pdftex/gentium
%{texmfdistdir}/fonts/tfm/public/gentium
%{texmfdistdir}/fonts/truetype/public/gentium
%{texmfdistdir}/tex/context/third/gentium
# gfsartemisia
%{texmfdistdir}/fonts/afm/public/gfsartemisia
%{texmfdistdir}/fonts/enc/dvips/gfsartemisia
%{texmfdistdir}/fonts/map/dvips/gfsartemisia
%{texmfdistdir}/fonts/opentype/public/gfsartemisia
%{texmfdistdir}/fonts/tfm/public/gfsartemisia
%{texmfdistdir}/fonts/type1/public/gfsartemisia
%{texmfdistdir}/fonts/vf/public/gfsartemisia
%{texmfdistdir}/tex/latex/gfsartemisia
# gfsbodoni
%{texmfdistdir}/fonts/afm/public/gfsbodoni
%{texmfdistdir}/fonts/enc/dvips/gfsbodoni
%{texmfdistdir}/fonts/map/dvips/gfsbodoni
%{texmfdistdir}/fonts/opentype/public/gfsbodoni
%{texmfdistdir}/fonts/tfm/public/gfsbodoni
%{texmfdistdir}/fonts/type1/public/gfsbodoni
%{texmfdistdir}/fonts/vf/public/gfsbodoni
%{texmfdistdir}/tex/latex/gfsbodoni
# gfscomplutum
%{texmfdistdir}/fonts/afm/public/gfscomplutum
%{texmfdistdir}/fonts/enc/dvips/gfscomplutum
%{texmfdistdir}/fonts/map/dvips/gfscomplutum
%{texmfdistdir}/fonts/opentype/public/gfscomplutum
%{texmfdistdir}/fonts/tfm/public/gfscomplutum
%{texmfdistdir}/fonts/type1/public/gfscomplutum
%{texmfdistdir}/fonts/vf/public/gfscomplutum
%{texmfdistdir}/tex/latex/gfscomplutum
# gfsdidot
%{texmfdistdir}/fonts/afm/public/gfsdidot
%{texmfdistdir}/fonts/enc/dvips/gfsdidot
%{texmfdistdir}/fonts/map/dvips/gfsdidot
%{texmfdistdir}/fonts/opentype/public/gfsdidot
%{texmfdistdir}/fonts/tfm/public/gfsdidot
%{texmfdistdir}/fonts/type1/public/gfsdidot
%{texmfdistdir}/fonts/vf/public/gfsdidot
%{texmfdistdir}/tex/latex/gfsdidot
# gfsneohellenic
%{texmfdistdir}/fonts/afm/public/gfsneohellenic
%{texmfdistdir}/fonts/enc/dvips/gfsneohellenic
%{texmfdistdir}/fonts/map/dvips/gfsneohellenic
%{texmfdistdir}/fonts/opentype/public/gfsneohellenic
%{texmfdistdir}/fonts/tfm/public/gfsneohellenic
%{texmfdistdir}/fonts/type1/public/gfsneohellenic
%{texmfdistdir}/fonts/vf/public/gfsneohellenic
%{texmfdistdir}/tex/latex/gfsneohellenic
# gfssolomos
%{texmfdistdir}/fonts/afm/public/gfssolomos
%{texmfdistdir}/fonts/enc/dvips/gfssolomos
%{texmfdistdir}/fonts/map/dvips/gfssolomos
%{texmfdistdir}/fonts/opentype/public/gfssolomos
%{texmfdistdir}/fonts/tfm/public/gfssolomos
%{texmfdistdir}/fonts/type1/public/gfssolomos
%{texmfdistdir}/fonts/vf/public/gfssolomos
%{texmfdistdir}/tex/latex/gfssolomos
# gnu-freefont
%{texmfdistdir}/fonts/opentype/public/gnu-freefont
%{texmfdistdir}/fonts/truetype/public/gnu-freefont
# greenpoint
%{texmfdistdir}/fonts/source/public/greenpoint
%{texmfdistdir}/fonts/tfm/public/greenpoint
# grotesq
%{texmfdistdir}/dvips/grotesq
%{texmfdistdir}/fonts/afm/urw/grotesq
%{texmfdistdir}/fonts/map/dvips/grotesq
%{texmfdistdir}/fonts/tfm/urw/grotesq
%{texmfdistdir}/fonts/type1/urw/grotesq
%{texmfdistdir}/fonts/vf/urw/grotesq
%{texmfdistdir}/tex/latex/grotesq
# hands
%{texmfdistdir}/fonts/source/public/hands
%{texmfdistdir}/fonts/tfm/public/hands
# hfbright
%{texmfdistdir}/dvips/hfbright
%{texmfdistdir}/fonts/afm/public/hfbright
%{texmfdistdir}/fonts/enc/dvips/hfbright
%{texmfdistdir}/fonts/map/dvips/hfbright
%{texmfdistdir}/fonts/type1/public/hfbright
# hfoldsty
%{texmfdistdir}/fonts/tfm/public/hfoldsty
%{texmfdistdir}/fonts/vf/public/hfoldsty
%{texmfdistdir}/tex/latex/hfoldsty
# ifsym
%{texmfdistdir}/fonts/source/public/ifsym
%{texmfdistdir}/fonts/tfm/public/ifsym
%{texmfdistdir}/tex/latex/ifsym
# inconsolata
%{texmfdistdir}/fonts/enc/dvips/inconsolata
%{texmfdistdir}/fonts/map/dvips/inconsolata
%{texmfdistdir}/fonts/opentype/public/inconsolata
%{texmfdistdir}/fonts/tfm/public/inconsolata
%{texmfdistdir}/fonts/type1/public/inconsolata
%{texmfdistdir}/tex/latex/inconsolata
# initials
%{texmfdistdir}/dvips/initials
%{texmfdistdir}/fonts/afm/public/initials
%{texmfdistdir}/fonts/map/dvips/initials
%{texmfdistdir}/fonts/tfm/public/initials
%{texmfdistdir}/fonts/type1/public/initials
%{texmfdistdir}/tex/latex/initials
# jablantile
%{texmfdistdir}/fonts/source/public/jablantile
# junicode
%{texmfdistdir}/fonts/truetype/public/junicode
# kixfont
%{texmfdistdir}/fonts/source/public/kixfont
%{texmfdistdir}/fonts/tfm/public/kixfont
# knuthotherfonts
%{texmfdistdir}/fonts/source/public/knuthotherfonts/committee
%{texmfdistdir}/fonts/source/public/knuthotherfonts/halftone
%{texmfdistdir}/fonts/source/public/knuthotherfonts/mfbook
# kpfonts
%{texmfdistdir}/fonts/afm/public/kpfonts
%{texmfdistdir}/fonts/enc/dvips/kpfonts
%{texmfdistdir}/fonts/enc/pdftex/kpfonts
%{texmfdistdir}/fonts/map/dvips/kpfonts
%{texmfdistdir}/fonts/source/public/kpfonts
%{texmfdistdir}/fonts/tfm/public/kpfonts
%{texmfdistdir}/fonts/type1/public/kpfonts
%{texmfdistdir}/fonts/vf/public/kpfonts
%{texmfdistdir}/tex/latex/kpfonts
# lfb
%{texmfdistdir}/fonts/source/public/lfb
%{texmfdistdir}/fonts/tfm/public/lfb
# libertine
%{texmfdistdir}/dvips/libertine
%{texmfdistdir}/fonts/afm/public/libertine
%{texmfdistdir}/fonts/enc/dvips/libertine
%{texmfdistdir}/fonts/map/dvips/libertine
%{texmfdistdir}/fonts/opentype/public/libertine
%{texmfdistdir}/fonts/tfm/public/libertine
%{texmfdistdir}/fonts/type1/public/libertine
%{texmfdistdir}/fonts/vf/public/libertine
%{texmfdistdir}/tex/latex/libertine
# libris
%{texmfdistdir}/fonts/afm/arkandis/libris
%{texmfdistdir}/fonts/enc/dvips/libris
%{texmfdistdir}/fonts/map/dvips/libris
%{texmfdistdir}/fonts/tfm/arkandis/libris
%{texmfdistdir}/fonts/type1/arkandis/libris
%{texmfdistdir}/fonts/vf/arkandis/libris
%{texmfdistdir}/tex/latex/libris
# linearA
%{texmfdistdir}/fonts/afm/public/linearA
%{texmfdistdir}/fonts/map/dvips/linearA
%{texmfdistdir}/fonts/tfm/public/linearA
%{texmfdistdir}/fonts/type1/public/linearA
%{texmfdistdir}/tex/latex/linearA
# lxfonts
%{texmfdistdir}/fonts/map/dvips/lxfonts
%{texmfdistdir}/fonts/source/public/lxfonts
%{texmfdistdir}/fonts/tfm/public/lxfonts
%{texmfdistdir}/fonts/type1/public/lxfonts
%{texmfdistdir}/tex/latex/lxfonts
# ly1
%{texmfdistdir}/fonts/enc/dvips/ly1
%{texmfdistdir}/fonts/map/dvips/ly1
%{texmfdistdir}/fonts/tfm/adobe/ly1
%{texmfdistdir}/fonts/vf/adobe/ly1
%{texmfdistdir}/tex/latex/ly1
%{texmfdistdir}/tex/plain/ly1
# mathabx
%{texmfdistdir}/fonts/source/public/mathabx
%{texmfdistdir}/fonts/tfm/public/mathabx
%{texmfdistdir}/tex/generic/mathabx
# mathdesign
%{texmfdistdir}/dvips/mathdesign
%{texmfdistdir}/fonts/afm/mathdesign/mdbch
%{texmfdistdir}/fonts/afm/mathdesign/mdput
%{texmfdistdir}/fonts/afm/mathdesign/mdugm
%{texmfdistdir}/fonts/map/dvips/mathdesign
%{texmfdistdir}/fonts/tfm/mathdesign/mdbch
%{texmfdistdir}/fonts/tfm/mathdesign/mdput
%{texmfdistdir}/fonts/tfm/mathdesign/mdugm
%{texmfdistdir}/fonts/type1/mathdesign/mdbch
%{texmfdistdir}/fonts/type1/mathdesign/mdput
%{texmfdistdir}/fonts/type1/mathdesign/mdugm
%{texmfdistdir}/fonts/vf/mathdesign/mdbch
%{texmfdistdir}/fonts/vf/mathdesign/mdput
%{texmfdistdir}/fonts/vf/mathdesign/mdugm
%{texmfdistdir}/tex/latex/mathdesign
# mnsymbol
%{texmfdistdir}/fonts/enc/dvips/mnsymbol
%{texmfdistdir}/fonts/map/dvips/mnsymbol
%{texmfdistdir}/fonts/map/vtex/mnsymbol
%{texmfdistdir}/fonts/opentype/public/mnsymbol
%{texmfdistdir}/fonts/source/public/mnsymbol
%{texmfdistdir}/fonts/tfm/public/mnsymbol
%{texmfdistdir}/fonts/type1/public/mnsymbol
%{texmfdistdir}/tex/latex/mnsymbol
# nkarta
%{texmfdistdir}/fonts/source/public/nkarta
%{texmfdistdir}/fonts/tfm/public/nkarta
%{texmfdistdir}/metapost/nkarta
# ocherokee
%{texmfdistdir}/fonts/afm/public/ocherokee
%{texmfdistdir}/fonts/map/dvips/ocherokee
%{texmfdistdir}/fonts/ofm/public/ocherokee
%{texmfdistdir}/fonts/ovf/public/ocherokee
%{texmfdistdir}/fonts/ovp/public/ocherokee
%{texmfdistdir}/fonts/tfm/public/ocherokee
%{texmfdistdir}/fonts/type1/public/ocherokee
%{texmfdistdir}/omega/ocp/ocherokee
%{texmfdistdir}/omega/otp/ocherokee
# ogham
%{texmfdistdir}/fonts/source/public/ogham
%{texmfdistdir}/fonts/tfm/public/ogham
# oinuit
%{texmfdistdir}/fonts/map/dvips/oinuit
%{texmfdistdir}/fonts/ofm/public/oinuit
%{texmfdistdir}/fonts/ovf/public/oinuit
%{texmfdistdir}/fonts/tfm/public/oinuit
%{texmfdistdir}/fonts/type1/public/oinuit
%{texmfdistdir}/omega/ocp/oinuit
%{texmfdistdir}/tex/lambda/oinuit
# oldlatin
%{texmfdistdir}/fonts/source/public/oldlatin
%{texmfdistdir}/fonts/tfm/public/oldlatin
# oldstandard
%{texmfdistdir}/fonts/opentype/public/oldstandard
# orkhun
%{texmfdistdir}/fonts/source/public/orkhun
%{texmfdistdir}/fonts/tfm/public/orkhun
# pacioli
%{texmfdistdir}/fonts/source/public/pacioli
%{texmfdistdir}/fonts/tfm/public/pacioli
%{texmfdistdir}/tex/latex/pacioli
# phaistos
%{texmfdistdir}/fonts/afm/public/phaistos
%{texmfdistdir}/fonts/map/dvips/phaistos
%{texmfdistdir}/fonts/opentype/public/phaistos
%{texmfdistdir}/fonts/tfm/public/phaistos
%{texmfdistdir}/fonts/type1/public/phaistos
%{texmfdistdir}/tex/latex/phaistos
# phonetic
%{texmfdistdir}/fonts/source/public/phonetic
%{texmfdistdir}/fonts/tfm/public/phonetic
%{texmfdistdir}/tex/latex/phonetic
# pigpen
%{texmfdistdir}/fonts/map/dvips/pigpen
%{texmfdistdir}/fonts/source/public/pigpen
%{texmfdistdir}/fonts/tfm/public/pigpen
%{texmfdistdir}/fonts/type1/public/pigpen
%{texmfdistdir}/tex/latex/pigpen
# prodint
%{texmfdistdir}/fonts/afm/public/prodint
%{texmfdistdir}/fonts/map/dvips/prodint
%{texmfdistdir}/fonts/tfm/public/prodint
%{texmfdistdir}/fonts/type1/public/prodint
%{texmfdistdir}/tex/latex/prodint
# psafm
%{texmfdistdir}/fonts/afm/itc/psafm/stonesan
# punk
%{texmfdistdir}/fonts/source/public/punk
%{texmfdistdir}/fonts/tfm/public/punk
# recycle
%{texmfdistdir}/fonts/map/dvips/recycle
%{texmfdistdir}/fonts/source/public/recycle
%{texmfdistdir}/fonts/tfm/public/recycle
%{texmfdistdir}/fonts/type1/public/recycle
%{texmfdistdir}/tex/latex/recycle
# romande
%{texmfdistdir}/fonts/afm/arkandis/romande
%{texmfdistdir}/fonts/enc/dvips/romande
%{texmfdistdir}/fonts/map/dvips/romande
%{texmfdistdir}/fonts/tfm/arkandis/romande
%{texmfdistdir}/fonts/type1/arkandis/romande
%{texmfdistdir}/fonts/vf/arkandis/romande
%{texmfdistdir}/tex/latex/romande
# rsfso
%{texmfdistdir}/fonts/map/dvips/rsfso
%{texmfdistdir}/fonts/tfm/public/rsfso
%{texmfdistdir}/fonts/vf/public/rsfso
%{texmfdistdir}/tex/latex/public/rsfso
# sauter
%{texmfdistdir}/fonts/source/public/sauter
# sauterfonts
%{texmfdistdir}/tex/latex/sauterfonts
# semaphor
%{texmfdistdir}/fonts/afm/public/semaphor
%{texmfdistdir}/fonts/enc/dvips/semaphor
%{texmfdistdir}/fonts/map/dvips/semaphor
%{texmfdistdir}/fonts/opentype/public/semaphor
%{texmfdistdir}/fonts/source/public/semaphor
%{texmfdistdir}/fonts/tfm/public/semaphor
%{texmfdistdir}/fonts/type1/public/semaphor
%{texmfdistdir}/tex/context/third/semaphor
%{texmfdistdir}/tex/latex/semaphor
%{texmfdistdir}/tex/plain/semaphor
# skull
%{texmfdistdir}/fonts/source/public/skull
%{texmfdistdir}/tex/latex/skull
# staves
%{texmfdistdir}/fonts/map/dvips/staves
%{texmfdistdir}/fonts/tfm/public/staves
%{texmfdistdir}/fonts/type1/public/staves
%{texmfdistdir}/tex/latex/staves
# stix
%{texmfdistdir}/fonts/opentype/public/stix
# tapir
%{texmfdistdir}/fonts/source/public/tapir
%{texmfdistdir}/fonts/type1/public/tapir
# tengwarscript
%{texmfdistdir}/fonts/enc/dvips/tengwarscript
%{texmfdistdir}/fonts/map/dvips/tengwarscript
%{texmfdistdir}/fonts/tfm/public/tengwarscript
%{texmfdistdir}/fonts/vf/public/tengwarscript
%{texmfdistdir}/tex/latex/tengwarscript
# tpslifonts
%{texmfdistdir}/tex/latex/tpslifonts
# trajan
%{texmfdistdir}/fonts/afm/public/trajan
%{texmfdistdir}/fonts/map/dvips/trajan
%{texmfdistdir}/fonts/tfm/public/trajan
%{texmfdistdir}/fonts/type1/public/trajan
%{texmfdistdir}/tex/latex/trajan
# txfontsb
%{texmfdistdir}/fonts/afm/public/txfontsb
%{texmfdistdir}/fonts/enc/dvips/txfontsb
%{texmfdistdir}/fonts/map/dvips/txfontsb
%{texmfdistdir}/fonts/tfm/public/txfontsb
%{texmfdistdir}/fonts/type1/public/txfontsb
%{texmfdistdir}/fonts/vf/public/txfontsb
%{texmfdistdir}/tex/latex/txfontsb
# umtypewriter
%{texmfdistdir}/fonts/opentype/public/umtypewriter
# universa
%{texmfdistdir}/fonts/source/public/universa
%{texmfdistdir}/fonts/tfm/public/universa
%{texmfdistdir}/tex/latex/universa
# urwchancal
%{texmfdistdir}/fonts/tfm/urw/urwchancal
%{texmfdistdir}/fonts/vf/urw/urwchancal
%{texmfdistdir}/tex/latex/urwchancal
# venturisadf
%{texmfdistdir}/fonts/afm/arkandis/venturis
%{texmfdistdir}/fonts/afm/arkandis/venturis2
%{texmfdistdir}/fonts/afm/arkandis/venturisold
%{texmfdistdir}/fonts/afm/arkandis/venturissans
%{texmfdistdir}/fonts/afm/arkandis/venturissans2
%{texmfdistdir}/fonts/enc/dvips/venturisadf
%{texmfdistdir}/fonts/map/dvips/venturis
%{texmfdistdir}/fonts/map/dvips/venturis2
%{texmfdistdir}/fonts/map/dvips/venturisold
%{texmfdistdir}/fonts/map/dvips/venturissans
%{texmfdistdir}/fonts/map/dvips/venturissans2
%{texmfdistdir}/fonts/tfm/arkandis/venturis
%{texmfdistdir}/fonts/tfm/arkandis/venturis2
%{texmfdistdir}/fonts/tfm/arkandis/venturisold
%{texmfdistdir}/fonts/tfm/arkandis/venturissans
%{texmfdistdir}/fonts/tfm/arkandis/venturissans2
%{texmfdistdir}/fonts/type1/arkandis/venturis
%{texmfdistdir}/fonts/type1/arkandis/venturis2
%{texmfdistdir}/fonts/type1/arkandis/venturisold
%{texmfdistdir}/fonts/type1/arkandis/venturissans
%{texmfdistdir}/fonts/type1/arkandis/venturissans2
%{texmfdistdir}/fonts/vf/arkandis/venturis
%{texmfdistdir}/fonts/vf/arkandis/venturis2
%{texmfdistdir}/fonts/vf/arkandis/venturisold
%{texmfdistdir}/fonts/vf/arkandis/venturissans
%{texmfdistdir}/fonts/vf/arkandis/venturissans2
%{texmfdistdir}/tex/latex/venturis
%{texmfdistdir}/tex/latex/venturis2
%{texmfdistdir}/tex/latex/venturisadf
%{texmfdistdir}/tex/latex/venturisold
%{texmfdistdir}/tex/latex/venturissans
%{texmfdistdir}/tex/latex/venturissans2
# wsuipa
%{texmfdistdir}/fonts/source/public/wsuipa
%{texmfdistdir}/fonts/tfm/public/wsuipa
%{texmfdistdir}/tex/latex/wsuipa
# xits
%{texmfdistdir}/fonts/opentype/public/xits
# yfonts
%{texmfdistdir}/tex/latex/yfonts

%post		-n texlive-fontsextra
sed -i	-e 's/^#! \(MixedMap allrunes.map\)/\1/'	\
	-e 's/^#! \(Map uaq.map\)/\1/'	\
	-e 's/^#! \(Map antt.map\)/\1/'	\
	-e 's/^#! \(Map archaicprw.map\)/\1/'	\
	-e 's/^#! \(Map arev.map\)/\1/'	\
	-e 's/^#! \(Map ascii.map\)/\1/'	\
	-e 's/^#! \(Map augie.map\)/\1/'	\
	-e 's/^#! \(Map auncial.map\)/\1/'	\
	-e 's/^#! \(Map aurical.map\)/\1/'	\
	-e 's/^#! \(Map ybv.map\)/\1/'	\
	-e 's/^#! \(Map belleek.map\)/\1/'	\
	-e 's/^#! \(Map bera.map\)/\1/'	\
	-e 's/^#! \(Map sqrcaps.map\)/\1/'	\
	-e 's/^#! \(Map boondox.map\)/\1/'	\
	-e 's/^#! \(Map pbsi.map\)/\1/'	\
	-e 's/^#! \(Map cantarell.map\)/\1/'	\
	-e 's/^#! \(Map cmin.map\)/\1/'	\
	-e 's/^#! \(Map ccicons.map\)/\1/'	\
	-e 's/^#! \(Map clm.map\)/\1/'	\
	-e 's/^#! \(Map cm-lgc.map\)/\1/'	\
	-e 's/^#! \(MixedMap cmll.map\)/\1/'	\
	-e 's/^#! \(Map cyklop.map\)/\1/'	\
	-e 's/^#! \(Map dictsym.map\)/\1/'	\
	-e 's/^#! \(Map dstroke.map\)/\1/'	\
	-e 's/^#! \(Map epigrafica.map\)/\1/'	\
	-e 's/^#! \(Map ESSTIX.map\)/\1/'	\
	-e 's/^#! \(Map esvect.map\)/\1/'	\
	-e 's/^#! \(Map fdsymbol.map\)/\1/'	\
	-e 's/^#! \(Map fge.map\)/\1/'	\
	-e 's/^#! \(Map foekfont.map\)/\1/'	\
	-e 's/^#! \(Map fonetika.map\)/\1/'	\
	-e 's/^#! \(Map fourier.map\)/\1/'	\
	-e 's/^#! \(Map fourier-utopia-expert.map\)/\1/'	\
	-e 's/^#! \(Map gfsartemisia.map\)/\1/'	\
	-e 's/^#! \(Map gfsbodoni.map\)/\1/'	\
	-e 's/^#! \(Map gfscomplutum.map\)/\1/'	\
	-e 's/^#! \(Map gfsdidot.map\)/\1/'	\
	-e 's/^#! \(Map gfsneohellenic.map\)/\1/'	\
	-e 's/^#! \(Map gfssolomos.map\)/\1/'	\
	-e 's/^#! \(Map ugq.map\)/\1/'	\
	-e 's/^#! \(MixedMap hfbright.map\)/\1/'	\
	-e 's/^#! \(Map fi4.map\)/\1/'	\
	-e 's/^#! \(Map Acorn.map\)/\1/'	\
	-e 's/^#! \(Map AnnSton.map\)/\1/'	\
	-e 's/^#! \(Map ArtNouv.map\)/\1/'	\
	-e 's/^#! \(Map ArtNouvc.map\)/\1/'	\
	-e 's/^#! \(Map Carrickc.map\)/\1/'	\
	-e 's/^#! \(Map Eichenla.map\)/\1/'	\
	-e 's/^#! \(Map Eileen.map\)/\1/'	\
	-e 's/^#! \(Map EileenBl.map\)/\1/'	\
	-e 's/^#! \(Map Elzevier.map\)/\1/'	\
	-e 's/^#! \(Map GotIn.map\)/\1/'	\
	-e 's/^#! \(Map GoudyIn.map\)/\1/'	\
	-e 's/^#! \(Map Kinigcap.map\)/\1/'	\
	-e 's/^#! \(Map Konanur.map\)/\1/'	\
	-e 's/^#! \(Map Kramer.map\)/\1/'	\
	-e 's/^#! \(Map MorrisIn.map\)/\1/'	\
	-e 's/^#! \(Map Nouveaud.map\)/\1/'	\
	-e 's/^#! \(Map Romantik.map\)/\1/'	\
	-e 's/^#! \(Map Rothdn.map\)/\1/'	\
	-e 's/^#! \(Map RoyalIn.map\)/\1/'	\
	-e 's/^#! \(Map Sanremo.map\)/\1/'	\
	-e 's/^#! \(Map Starburst.map\)/\1/'	\
	-e 's/^#! \(Map Typocaps.map\)/\1/'	\
	-e 's/^#! \(Map Zallman.map\)/\1/'	\
	-e 's/^#! \(Map kpfonts.map\)/\1/'	\
	-e 's/^#! \(Map libertine.map\)/\1/'	\
	-e 's/^#! \(Map yly.map\)/\1/'	\
	-e 's/^#! \(Map linearA.map\)/\1/'	\
	-e 's/^#! \(MixedMap lxfonts.map\)/\1/'	\
	-e 's/^#! \(Map mdbch.map\)/\1/'	\
	-e 's/^#! \(Map mdput.map\)/\1/'	\
	-e 's/^#! \(Map mdugm.map\)/\1/'	\
	-e 's/^#! \(Map MnSymbol.map\)/\1/'	\
	-e 's/^#! \(Map cherokee.map\)/\1/'	\
	-e 's/^#! \(Map oinuit.map\)/\1/'	\
	-e 's/^#! \(Map phaistos.map\)/\1/'	\
	-e 's/^#! \(MixedMap pigpen.map\)/\1/'	\
	-e 's/^#! \(Map prodint.map\)/\1/'	\
	-e 's/^#! \(Map recycle.map\)/\1/'	\
	-e 's/^#! \(Map yrd.map\)/\1/'	\
	-e 's/^#! \(MixedMap semaf.map\)/\1/'	\
	-e 's/^#! \(Map icelandic.map\)/\1/'	\
	-e 's/^#! \(MixedMap trajan.map\)/\1/'	\
	-e 's/^#! \(Map gptimes.map\)/\1/'	\
	-e 's/^#! \(Map yv1.map\)/\1/'	\
	-e 's/^#! \(Map yv2.map\)/\1/'	\
	-e 's/^#! \(Map yv3.map\)/\1/'	\
	-e 's/^#! \(Map yvo.map\)/\1/'	\
	-e 's/^#! \(Map yvt.map\)/\1/'	\
	 %{texmfdir}/web2c/updmap.cfg
if [ -x %{texmfbindir}/updmap-sys ]; then
    %{texmfbindir}/updmap-sys --syncwithtrees > /dev/null
fi

%postun		-n texlive-fontsextra
if [ -f %{texmfdir}/web2c/updmap.cfg ]; then
sed -i	-e 's/^\(MixedMap allrunes.map\)/#! \1/'	\
	-e 's/^\(Map uaq.map\)/#! \1/'	\
	-e 's/^\(Map antt.map\)/#! \1/'	\
	-e 's/^\(Map archaicprw.map\)/#! \1/'	\
	-e 's/^\(Map arev.map\)/#! \1/'	\
	-e 's/^\(Map ascii.map\)/#! \1/'	\
	-e 's/^\(Map augie.map\)/#! \1/'	\
	-e 's/^\(Map auncial.map\)/#! \1/'	\
	-e 's/^\(Map aurical.map\)/#! \1/'	\
	-e 's/^\(Map ybv.map\)/#! \1/'	\
	-e 's/^\(Map belleek.map\)/#! \1/'	\
	-e 's/^\(Map bera.map\)/#! \1/'	\
	-e 's/^\(Map sqrcaps.map\)/#! \1/'	\
	-e 's/^\(Map boondox.map\)/#! \1/'	\
	-e 's/^\(Map pbsi.map\)/#! \1/'	\
	-e 's/^\(Map cantarell.map\)/#! \1/'	\
	-e 's/^\(Map cmin.map\)/#! \1/'	\
	-e 's/^\(Map ccicons.map\)/#! \1/'	\
	-e 's/^\(Map clm.map\)/#! \1/'	\
	-e 's/^\(Map cm-lgc.map\)/#! \1/'	\
	-e 's/^\(MixedMap cmll.map\)/#! \1/'	\
	-e 's/^\(Map cyklop.map\)/#! \1/'	\
	-e 's/^\(Map dictsym.map\)/#! \1/'	\
	-e 's/^\(Map dstroke.map\)/#! \1/'	\
	-e 's/^\(Map epigrafica.map\)/#! \1/'	\
	-e 's/^\(Map ESSTIX.map\)/#! \1/'	\
	-e 's/^\(Map esvect.map\)/#! \1/'	\
	-e 's/^\(Map fdsymbol.map\)/#! \1/'	\
	-e 's/^\(Map fge.map\)/#! \1/'	\
	-e 's/^\(Map foekfont.map\)/#! \1/'	\
	-e 's/^\(Map fonetika.map\)/#! \1/'	\
	-e 's/^\(Map fourier.map\)/#! \1/'	\
	-e 's/^\(Map fourier-utopia-expert.map\)/#! \1/'	\
	-e 's/^\(Map gfsartemisia.map\)/#! \1/'	\
	-e 's/^\(Map gfsbodoni.map\)/#! \1/'	\
	-e 's/^\(Map gfscomplutum.map\)/#! \1/'	\
	-e 's/^\(Map gfsdidot.map\)/#! \1/'	\
	-e 's/^\(Map gfsneohellenic.map\)/#! \1/'	\
	-e 's/^\(Map gfssolomos.map\)/#! \1/'	\
	-e 's/^\(Map ugq.map\)/#! \1/'	\
	-e 's/^\(MixedMap hfbright.map\)/#! \1/'	\
	-e 's/^\(Map fi4.map\)/#! \1/'	\
	-e 's/^\(Map Acorn.map\)/#! \1/'	\
	-e 's/^\(Map AnnSton.map\)/#! \1/'	\
	-e 's/^\(Map ArtNouv.map\)/#! \1/'	\
	-e 's/^\(Map ArtNouvc.map\)/#! \1/'	\
	-e 's/^\(Map Carrickc.map\)/#! \1/'	\
	-e 's/^\(Map Eichenla.map\)/#! \1/'	\
	-e 's/^\(Map Eileen.map\)/#! \1/'	\
	-e 's/^\(Map EileenBl.map\)/#! \1/'	\
	-e 's/^\(Map Elzevier.map\)/#! \1/'	\
	-e 's/^\(Map GotIn.map\)/#! \1/'	\
	-e 's/^\(Map GoudyIn.map\)/#! \1/'	\
	-e 's/^\(Map Kinigcap.map\)/#! \1/'	\
	-e 's/^\(Map Konanur.map\)/#! \1/'	\
	-e 's/^\(Map Kramer.map\)/#! \1/'	\
	-e 's/^\(Map MorrisIn.map\)/#! \1/'	\
	-e 's/^\(Map Nouveaud.map\)/#! \1/'	\
	-e 's/^\(Map Romantik.map\)/#! \1/'	\
	-e 's/^\(Map Rothdn.map\)/#! \1/'	\
	-e 's/^\(Map RoyalIn.map\)/#! \1/'	\
	-e 's/^\(Map Sanremo.map\)/#! \1/'	\
	-e 's/^\(Map Starburst.map\)/#! \1/'	\
	-e 's/^\(Map Typocaps.map\)/#! \1/'	\
	-e 's/^\(Map Zallman.map\)/#! \1/'	\
	-e 's/^\(Map kpfonts.map\)/#! \1/'	\
	-e 's/^\(Map libertine.map\)/#! \1/'	\
	-e 's/^\(Map yly.map\)/#! \1/'	\
	-e 's/^\(Map linearA.map\)/#! \1/'	\
	-e 's/^\(MixedMap lxfonts.map\)/#! \1/'	\
	-e 's/^\(Map mdbch.map\)/#! \1/'	\
	-e 's/^\(Map mdput.map\)/#! \1/'	\
	-e 's/^\(Map mdugm.map\)/#! \1/'	\
	-e 's/^\(Map MnSymbol.map\)/#! \1/'	\
	-e 's/^\(Map cherokee.map\)/#! \1/'	\
	-e 's/^\(Map oinuit.map\)/#! \1/'	\
	-e 's/^\(Map phaistos.map\)/#! \1/'	\
	-e 's/^\(MixedMap pigpen.map\)/#! \1/'	\
	-e 's/^\(Map prodint.map\)/#! \1/'	\
	-e 's/^\(Map recycle.map\)/#! \1/'	\
	-e 's/^\(Map yrd.map\)/#! \1/'	\
	-e 's/^\(MixedMap semaf.map\)/#! \1/'	\
	-e 's/^\(Map icelandic.map\)/#! \1/'	\
	-e 's/^\(MixedMap trajan.map\)/#! \1/'	\
	-e 's/^\(Map gptimes.map\)/#! \1/'	\
	-e 's/^\(Map yv1.map\)/#! \1/'	\
	-e 's/^\(Map yv2.map\)/#! \1/'	\
	-e 's/^\(Map yv3.map\)/#! \1/'	\
	-e 's/^\(Map yvo.map\)/#! \1/'	\
	-e 's/^\(Map yvt.map\)/#! \1/'	\
	 %{texmfdir}/web2c/updmap.cfg
	 %{texmfdir}/web2c/updmap.cfg
    if [ -x %{texmfbindir}/updmap-sys ]; then
	%{texmfbindir}/updmap-sys --syncwithtrees > /dev/null
    fi
fi

#-----------------------------------------------------------------------
%package	-n texlive-source
Summary:	Tex Live source files
Group:		Publishing
Requires:	texlive-texmf = %{version}-%{release}

%description	-n texlive-source
TeX Live is an easy way to get up and running with the TeX document
production system. It provides a comprehensive TeX system. It includes
all the major TeX-related programs, macro packages, and fonts that are
free software, including support for many languages around the world.

%files		-n texlive-source
%defattr(-,root,root,-)
%{texmfdistdir}/source

#-----------------------------------------------------------------------
%prep
%setup -q -n texlive-%{version}-texmf

perl -pi -e 's%^(TEXMFMAIN\s+= ).*%$1%{texmfdir}%;'			  \
	 -e 's%^(TEXMFDIST\s+= ).*%$1%{texmfdistdir}%;'			  \
	 -e 's%^(TEXMFLOCAL\s+= ).*%$1%{texmflocaldir}%;'		  \
	 -e 's%^(TEXMFSYSVAR\s+= ).*%$1%{texmfvardir}%;'		  \
	 -e 's%^(TEXMFSYSCONFIG\s+= ).*%$1%{texmfconfdir}%;'		  \
	 -e 's%^(TEXMFHOME\s+= ).*%$1\$HOME/texmf%;'			  \
	 -e 's%^(TEXMFVAR\s+= ).*%$1\$HOME/.texlive2011/texmf-var%;'	  \
	 -e 's%^(TEXMFCONFIG\s+= ).*%$1\$HOME/.texlive2011/texmf-config%;'\
	 -e 's%^(OSFONTDIR\s+= ).*%$1%{_datadir}/fonts%;'		  \
	texmf/web2c/texmf.cnf

perl -pi -e 's%^(\s*TEXMFMAIN\s+=\s+").*%$1%{texmfdir}",%;'				\
	 -e 's%\bTEXMFCONTEXT\b%TEXMFDIST%g;'						\
	 -e 's%^(\s*TEXMFDIST\s+=\s+).*%$1"%{texmfdistdir}",%;'				\
	 -e 's%^(\s*TEXMFLOCAL\s+=\s+).*%$1"%{texmflocaldir}",%;'			\
	 -e 's%^(\s*TEXMFSYSVAR\s+=\s+).*%$1"%{texmfvardir}",%;'			\
	 -e 's%^(\s*TEXMFSYSCONFIG\s+=\s+).*%$1"%{texmfconfdir}",%;'			\
	 -e 's%^(\s*TEXMFHOME\s+=\s+").*%$1\$HOME/texmf",%;'				\
	 -e 's%^(\s*TEXMFVAR\s+=\s+").*%$1\$HOME/.texlive2011/texmf-var",%;'		\
	 -e 's%^(\s*TEXMFCONFIG\s+=\s+").*%$1\$HOME/.texlive2011/texmf-config",%;'	\
	 -e 's%^(\s*FONTCONFIG_PATH\s+=\s+").*%$1%{_sysconfdir}/fonts",%;'		\
	 -e 's|^local texmflocal.*$||;'							\
	 -e 's|^texmflocal.*$||;'							\
	texmf/web2c/texmfcnf.lua

perl -pi -e 's%^# (viewer_pdf = )xpdf.*%$1xdg-open%;'	\
	texmf-dist/texdoc/texdoc.cnf

%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

#-----------------------------------------------------------------------
%build

#-----------------------------------------------------------------------
%install
mkdir -p %{buildroot}%{texmfdir}
cp -far texmf/* %{buildroot}%{texmfdir}
mkdir -p %{buildroot}%{texmfdistdir}
cp -far texmf-dist/* %{buildroot}%{texmfdistdir}

mkdir -p %{buildroot}%{texmfbindir}
pushd %{buildroot}%{texmfbindir}
    ln -sf %{texmfdir}/scripts/a2ping/a2ping.pl a2ping
    ln -sf %{texmfdistdir}/scripts/fontools/afm2afm afm2afm
    ln -sf %{texmfdistdir}/scripts/bundledoc/arlatex arlatex
    ln -sf %{texmfdistdir}/scripts/authorindex/authorindex authorindex
    ln -sf %{texmfdistdir}/scripts/fontools/autoinst autoinst
    ln -sf %{texmfdistdir}/scripts/bibexport/bibexport.sh bibexport
    ln -sf %{texmfdistdir}/scripts/bundledoc/bundledoc bundledoc
    ln -sf %{texmfdistdir}/scripts/cachepic/cachepic.tlu cachepic
    ln -sf %{texmfdistdir}/scripts/fontools/cmap2enc cmap2enc
    ln -sf %{texmfdistdir}/scripts/de-macro/de-macro de-macro
    ln -sf %{texmfdistdir}/scripts/dviasm/dviasm.py dviasm
    ln -sf %{texmfdir}/scripts/tetex/e2pall.pl e2pall
    ln -sf %{texmfdistdir}/scripts/ebong/ebong.py ebong
    ln -sf %{texmfdistdir}/scripts/epspdf/epspdf.rb epspdf
    ln -sf %{texmfdistdir}/scripts/epspdf/epspdftk.tcl epspdftk
    ln -sf %{texmfdistdir}/scripts/epstopdf/epstopdf.pl epstopdf
    ln -sf %{texmfdistdir}/scripts/fig4latex/fig4latex fig4latex
    ln -sf %{texmfdistdir}/scripts/findhyph/findhyph findhyph
    ln -sf %{texmfdistdir}/scripts/fontools/font2afm font2afm
    ln -sf %{texmfdistdir}/scripts/fragmaster/fragmaster.pl fragmaster
%if !%{with_system_tex4ht}
    ln -sf %{texmfdistdir}/scripts/tex4ht/ht.sh ht
    ln -sf %{texmfdistdir}/scripts/tex4ht/htcontext.sh htcontext
    ln -sf %{texmfdistdir}/scripts/tex4ht/htlatex.sh htlatex
    ln -sf %{texmfdistdir}/scripts/tex4ht/htmex.sh htmex
    ln -sf %{texmfdistdir}/scripts/tex4ht/httex.sh httex
    ln -sf %{texmfdistdir}/scripts/tex4ht/httexi.sh httexi
    ln -sf %{texmfdistdir}/scripts/tex4ht/htxelatex.sh htxelatex
    ln -sf %{texmfdistdir}/scripts/tex4ht/htxetex.sh htxetex
%endif
    ln -sf %{texmfdistdir}/scripts/latex2man/latex2man latex2man
    ln -sf %{texmfdistdir}/scripts/latexdiff/latexdiff.pl latexdiff
    ln -sf %{texmfdistdir}/scripts/latexdiff/latexdiff-vc.pl latexdiff-vc
    ln -sf %{texmfdistdir}/scripts/latexmk/latexmk.pl latexmk
    ln -sf %{texmfdistdir}/scripts/latexdiff/latexrevise.pl latexrevise
    ln -sf %{texmfdistdir}/scripts/listings-ext/listings-ext.sh listings-ext.sh
    ln -sf %{texmfdistdir}/scripts/glossaries/makeglossaries makeglossaries
    ln -sf %{texmfdistdir}/scripts/mathspic/mathspic.pl mathspic
%if !%{with_system_tex4ht}
    ln -sf %{texmfdistdir}/scripts/tex4ht/mk4ht.pl mk4ht
%endif
    ln -sf %{texmfdistdir}/scripts/mkgrkindex/mkgrkindex mkgrkindex
    ln -sf %{texmfdistdir}/scripts/mkjobtexmf/mkjobtexmf.pl mkjobtexmf
    ln -sf %{texmfdistdir}/scripts/luaotfload/mkluatexfontdb.lua mkluatexfontdb
    ln -sf %{texmfdistdir}/scripts/accfonts/mkt1font mkt1font
    ln -sf %{texmfdistdir}/scripts/context/perl/mptopdf.pl mptopdf
    ln -sf %{texmfdistdir}/scripts/fontools/ot2kpx ot2kpx
    ln -sf %{texmfdistdir}/scripts/pdfjam/pdf180 pdf180
    ln -sf %{texmfdistdir}/scripts/pdfjam/pdf270 pdf270
    ln -sf %{texmfdistdir}/scripts/pdfjam/pdf90 pdf90
    ln -sf %{texmfdistdir}/scripts/pax/pdfannotextractor.pl pdfannotextractor
    ln -sf %{texmfdistdir}/scripts/oberdiek/pdfatfi.pl pdfatfi
    ln -sf %{texmfdistdir}/scripts/pdfjam/pdfbook pdfbook
    ln -sf %{texmfdistdir}/scripts/pdfcrop/pdfcrop.pl pdfcrop
    ln -sf %{texmfdistdir}/scripts/pdfjam/pdfflip pdfflip
    ln -sf %{texmfdistdir}/scripts/pdfjam/pdfjam pdfjam
    ln -sf %{texmfdistdir}/scripts/pdfjam/pdfjam-pocketmod pdfjam-pocketmod
    ln -sf %{texmfdistdir}/scripts/pdfjam/pdfjam-slides3up pdfjam-slides3up
    ln -sf %{texmfdistdir}/scripts/pdfjam/pdfjam-slides6up pdfjam-slides6up
    ln -sf %{texmfdistdir}/scripts/pdfjam/pdfjoin pdfjoin
    ln -sf %{texmfdistdir}/scripts/pdfjam/pdfnup pdfnup
    ln -sf %{texmfdistdir}/scripts/pdfjam/pdfpun pdfpun
    ln -sf %{texmfdistdir}/scripts/ppower4/pdfthumb.tlu pdfthumb
    ln -sf %{texmfdistdir}/scripts/perltex/perltex.pl perltex
    ln -sf %{texmfdistdir}/scripts/fontools/pfm2kpx pfm2kpx
    ln -sf %{texmfdistdir}/scripts/pkfix/pkfix.pl pkfix
    ln -sf %{texmfdistdir}/scripts/pkfix-helper/pkfix-helper pkfix-helper
    ln -sf %{texmfdistdir}/scripts/ppower4/ppower4.tlu ppower4
    ln -sf %{texmfdistdir}/scripts/pst-pdf/ps4pdf ps4pdf
    ln -sf %{texmfdistdir}/scripts/pst2pdf/pst2pdf pst2pdf
    ln -sf %{texmfdistdir}/scripts/purifyeps/purifyeps purifyeps
    ln -sf epstopdf repstopdf
    ln -sf pdfcrop rpdfcrop
    ln -sf %{texmfdir}/scripts/texlive/rungs.tlu rungs
    ln -sf %{texmfdistdir}/scripts/fontools/showglyphs showglyphs
    ln -sf %{texmfdistdir}/scripts/splitindex/perl/splitindex.pl splitindex
    ln -sf %{texmfdir}/scripts/simpdftex/simpdftex simpdftex
    ln -sf %{texmfdistdir}/scripts/svn-multi/svn-multi.pl svn-multi
    ln -sf %{texmfdistdir}/scripts/texcount/texcount.pl texcount
    ln -sf %{texmfdistdir}/scripts/texdiff/texdiff texdiff
    ln -sf %{texmfdistdir}/scripts/texdirflatten/texdirflatten texdirflatten
    ln -sf %{texmfdir}/scripts/texdoc/texdoc.tlu texdoc
    ln -sf %{texmfdistdir}/scripts/texloganalyser/texloganalyser texloganalyser
    ln -sf %{texmfdistdir}/scripts/thumbpdf/thumbpdf.pl thumbpdf
    ln -sf %{texmfdistdir}/scripts/ulqda/ulqda.pl ulqda
    ln -sf %{texmfdistdir}/scripts/vpe/vpe.pl vpe
    ln -sf %{texmfdistdir}/scripts/accfonts/vpl2ovp vpl2ovp
    ln -sf %{texmfdistdir}/scripts/accfonts/vpl2vpl vpl2vpl
    ln -sf %{texmfdir}/scripts/tetex/updmap.pl updmap
popd

%if %mdkversion >= 201100
    mkdir -p %{buildroot}%{_datadir}/X11/app-defaults
    pushd %{buildroot}%{_datadir}/X11/app-defaults
	ln -sf %{texmfdir}/xdvi/XDvi XDvi
	cp %{SOURCE2} %{buildroot}%{_datadir}/X11/app-defaults
    popd
%endif

pushd %{buildroot}%{texmfdir}
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
    cp -f %{SOURCE3} .

    find doc/man \( -name Makefile -o -name \*.pdf \) -exec rm -f {} \;
%if %{with_system_psutils}
    rm -f doc/man/man1/{epsffit,extractres,fixdlsrps,fixfmps,fixmacps,fixpsditps,fixpspps,fixscribeps,fixtpps,fixwfwps,fixwpps,fixwwps,getafm,includeres,psbook,psmerge,psnup,psresize,psselect,pstops}.1
%endif

%if %mdkversion >= 201100
    mkdir -p %{buildroot}%{_mandir}
    mv -f doc/man/* %{buildroot}%{_mandir}
    mkdir -p %{buildroot}%{_infodir}
    mv -f doc/info/*.info %{buildroot}%{_infodir}
%endif
popd

pushd %{buildroot}%{texmfdistdir}
%if %{with_system_tex4ht}
    rm -fr tex4ht
%endif
    rm -f ls-R README
    # .in files in documentation confuse find-provides
    rm -f doc/bibtex/urlbst/*.in
popd

%if !%{with_system_tex4ht}
    %if %mdkversion >= 201100
	mkdir %{buildroot}%{_javadir}
	pushd %{buildroot}%{_javadir}
	    ln -sf %{texmfdistdir}/tex4ht/bin/tex4ht.jar tex4ht.jar
	popd
    %endif
%endif

tar zxf %{SOURCE4}
mkdir -p %{buildroot}%{texmfdir}/tlpkg
mv -f install-tl-*/tlpkg/TeXLive %{buildroot}%{texmfdir}/tlpkg

perl -pi -e 's|TEXMFROOT|TEXMFMAIN|g;'			\
    %{buildroot}%{texmfdir}/scripts/tetex/updmap.pl

mkdir -p %{buildroot}%{texmflocaldir}

#-----------------------------------------------------------------------
%clean
rm -rf %{buildroot}
