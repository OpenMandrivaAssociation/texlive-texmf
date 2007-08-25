%bcond_with     obsolete_tetex

%{!?_texmf_main: %global _texmf_main %{_datadir}/texmf}
%{!?_texmf_vendor: %global _texmf_vendor %{_datadir}/texmf-texlive}
%{!?_texmf_var: %global _texmf_var  %{_var}/lib/texmf}
%{!?_texmf_conf: %global _texmf_conf %{_sysconfdir}/texmf}
%{!?_texmf_local: %global _texmf_local %{_usr}/local/share/texmf}

Name:           texlive-texmf
Version:        2007
Release:        %mkrel 12
Epoch:          0
Summary:        Architecture independent parts of the TeX formatting system
Group:          Publishing
License:        Distributable
URL:            http://tug.org/texlive/
# rsync -avzH --exclude=.svn --exclude=bin tug.org::tldevsrc/Master .
# tar cvjf texlive-texmf-src.tar.bz2 Master
Source0:        texlive-texmf-src.tar.bz2
# Source1 is http://www.tug.org/texlive/Contents/inst/archive/texmf-var.zip
Source1:        texlive.texmf-var-%{version}.zip
Source2:        texlive.2007.ls-R
Source3:        texlive.var.2007.ls-R
Source4:        texlive.conf.2007.ls-R
Source5:        texlive.vendor.2007.ls-R
# missing files (note - Fedora installs this with a patch)
Source50:       dvips-config.generic
# Fedora
Patch0:         texlive-2007-badenv.patch
Patch1:         texlive-2007-tkdefaults.patch
# Suse
Patch300:       texlive-texmf.patch
# XXX: Needed for texinfo
%if %with obsolete_tetex
Provides:       tetex = 0:3.0
Conflicts:      tetex < 0:3.0
BuildConflicts: tetex < 0:3.0
%else
Provides:       tetex = 3.0
%endif
Provides:       latex-pgf = 0:1.01
Provides:       latex-xcolor = 0:2.00
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

%description
texlive-texmf is a texmf distribution based upon TeX Live. All of the files
contained in these packages are from the TeX Live zip files. The intent is to
provide a packaging similar in style and layout to teTeX.

%package common
Summary:        The basic texmf directory structure
Group:          Publishing

%description common
This package owns the basic directory structure of the texmf

%package context
Summary:        Document engineering system based on TeX
Group:          Publishing
Requires:       texlive-texmf-common = %{epoch}:%{version}-%{release}

%description context
CONTeXT is a document engineering system based on TeX. TeX is a
typesetting system and a program to typeset and produce documents.
CONTeXT is easy to use and enables you to make complex paper and
electronic documents.

%package cmsuper
Group:          Publishing
Summary:        The CM-Super font set
%if %with obsolete_tetex
Obsoletes:      tetex-cmsuper
%endif
Provides:       tetex-cmsuper
Requires:       texlive-texmf-common = %{epoch}:%{version}-%{release}

%description cmsuper
The CM-Super package contains Type 1 fonts converted from METAFONT
fonts and covers entire EC/TC, ECC and LH fonts (Computer Modern font
families). All European and Cyrillic writings are covered. Each Type 1
font program contains ALL glyphs from the following standard LaTeX
font encodings: T1, TS1, T2A, T2B, T2C, X2, and also Adobe
StandardEncoding (585 glyphs per non-SC font and 468 glyphs per SC
font), and could be reencoded to any of these encodings using standard
dvips or pdftex facilities (the corresponding support files are also
included).

%package afm
Group:          Publishing
Summary:        Texmf files needed for texlive-afm
%if %with obsolete_tetex
Obsoletes:      tetex-afm
%endif
Provides:       tetex-afm
Requires:       texlive-texmf-common = %{epoch}:%{version}-%{release}

%description afm
This package contains the components of the TEXMF tree needed for the
texlive-afm package.

%package doc
Group:          Publishing
Summary:        TeX documentation
%if %with obsolete_tetex
Obsoletes:      tetex-doc
%endif
Provides:       tetex-doc
Obsoletes:      texlive-doc
Provides:       texlive-doc
Requires:       texlive-texmf-common = %{epoch}:%{version}-%{release}

%description doc
This package contains the documentation for packages installed as part of
texlive. You should install this package if you are new to TeX and LaTeX,
and familiarize yourself with the use of the texdoc command.

%package dvipdfm
Group:          Publishing
Summary:        A DVI to PDF converter
Requires:       texlive-texmf-common = %{epoch}:%{version}-%{release}

%description dvipdfm
dvidpfm is a DVI to PDF translator for use with TeX.

%package dvips
Group:          Publishing
Summary:        Texmf files needed for texlive-dvips
%if %with obsolete_tetex
Conflicts:      tetex-dvipdfm < 1:3.0
Obsoletes:      tetex-dvips
%endif
Provides:       tetex-dvips
Requires:       texlive-texmf-common = %{epoch}:%{version}-%{release}

%description dvips
This package contains the components of the TEXMF tree needed for the
texlive-dvips package.

%package fonts
Group:          Publishing
Summary:        Texmf files needed for texlive-fonts
Requires:       texlive-texmf-dvips = %{epoch}:%{version}-%{release}

%description fonts
This package contains the components of the TEXMF tree needed for the
texlive-fonts package.

%package latex
Group:          Publishing
Summary:        Texmf files needed for texlive-latex
Requires:       texlive-texmf = %{epoch}:%{version}-%{release}
Requires:       texlive-texmf-common = %{epoch}:%{version}-%{release}
%if %with obsolete_tetex
Obsoletes:      tetex-latex
%endif
Provides:       tetex-latex
%if %with obsolete_tetex
Obsoletes:      tetex-IEEEtran
%endif
Provides:       tetex-IEEEtran
%if %with obsolete_tetex
Obsoletes:      latex-beamer < 0:3.07
%endif
Provides:       latex-beamer = 0:3.07

%description latex
This package contains the components of the TEXMF tree needed for the
texlive-latex package.

%package usrlocal
Group:          Publishing
Summary:        Virtual package for placing local system-wide teTeX files
%if %with obsolete_tetex
Obsoletes:      tetex-usrlocal
%endif
Provides:       tetex-usrlocal

%description usrlocal
This packages provides just the directory %{_texmf_local}
which is defined by the var TEXMFLOCAL in the default config file
and can be used for system-wide texlive files.

%package jadetex
Summary:        TeX macros used by Jade TeX output
Group:          Publishing
Requires:       texlive-texmf-common = %{epoch}:%{version}-%{release}

%description jadetex
JadeTeX contains the additional LaTeX macros necessary for taking Jade
TeX output files and processing them as TeX files, to obtain DVI, Postscript
or PDF files for example.

%package xmltex
Summary:        Namespace-aware XML parser written in TeX
Group:          Publishing
Requires:       texlive-texmf-common = %{epoch}:%{version}-%{release}

%description xmltex
Namespace-aware XML parser written in TeX. This package
also includes passivetex macros, which can be used to process an XML
document which results from an XSL trasformation to formatting objects.

%prep
%setup -q -n Master
%{__chmod} -Rf a+rX,u+w,g-w,o-w .

mkdir texmf-var
unzip -d texmf-var %{SOURCE1}
install -m644 %{SOURCE50} texmf-var/dvips/config/config.generic

%patch0 -p0
%patch1 -p0
%patch300 -p0

# these may be useful to hang onto
mkdir -p texmf/doc/from_texlive
mv texmf/lists texmf/doc/from_texlive/

# we use web2c/fmutil.cnf for defaults
rm texmf/fmtutil/*

# these we do not want
# - they are owned by main package in /usr/bin
rm -r texmf/scripts/tetex
rm -r texmf/scripts/thumbpdf
rm -r texmf/scripts/pdfcrop

# setup texmf.cnf properly
pushd texmf/web2c
%{__sed} -i 's?^TEXMFMAIN =.*?TEXMFMAIN = %{_texmf_main}?' texmf.cnf
%{__sed} -i 's?^TEXMFDIST =.*?TEXMFDIST = %{_texmf_vendor}?' texmf.cnf
%{__sed} -i 's?^TEXMFSYSVAR =.*?TEXMFSYSVAR = %{_texmf_var}?' texmf.cnf
%{__sed} -i 's?^TEXMFSYSCONFIG =.*?TEXMFSYSCONFIG = %{_texmf_conf}?' texmf.cnf
%{__sed} -i 's?^TEXMFVENDOR =.*?TEXMFVENDOR = %{_texmf_vendor}?' texmf.cnf

%{__sed} -i 's?^TEXMFMAIN .*?TEXMFMAIN     = %{_texmf_main}?' context.cnf
%{__sed} -i 's?^VARTEXMF .*?VARTEXMF      = %{_texmf_var}?' context.cnf
%{__sed} -i 's?^TEXMFVENDOR .*?TEXMFVENDOR   = %{_texmf_vendor}?' context.cnf
popd

# nuke these
rm -r source
rm -r texmf-dist/source
rm texmf/web2c/texmf.cnf-4WIN
rm texmf/texdoctk/texdocrc-win32.defaults

install -d -m755 texmf-var/fonts/map/{dvipdfm,dvips,pdftex}/updmap
# for ghosting
touch texmf-var/fonts/map/dvipdfm/updmap/{dvipdfm_dl14.map,dvipdfm.map,dvipdfm_ndl14.map}
touch texmf-var/fonts/map/dvips/updmap/{builtin35.map,ps2pk.map,psfonts_pk.map,download35.map,psfonts.map,psfonts_t1.map}
touch texmf-var/fonts/map/pdftex/updmap/{pdftex_dl14.map,pdftex.map,pdftex_ndl14.map}

# We really don't want these imho
rm -r texmf-dist/fonts/pk && mkdir texmf-dist/fonts/pk
# We want these but in the right place
mv texmf/doc/info/{tds,eplain}.info .
# now nuke the info dir
rm -r texmf/doc/info

# Create symlinks for Euler fonts (RH #9782)
pushd texmf-dist/tex/latex/amsfonts
for i in ex f r s ; do
  ln -sf ueu${i}.fd Ueu${i}.fd
done
popd

# fix the bloody permissions - Grrrr
for toplevel in texmf texmf-dist texmf-var; do
  for directory in `find ${toplevel} -type d -print`; do
    chmod 755 ${directory}
  done
  for file in `find ${toplevel} -type f -print`; do
    if [ ! -x ${file} ]; then
      chmod 644 ${file}
    else
      chmod 755 ${file}
    fi
  done
done

# fix the ruby scripts
for ruby in `find texmf-dist/scripts/context/ruby/ -name *.rb`; do
  if [ `head -1 $ruby |grep -c "^#!"` -eq 1 ]; then
    chmod 755 ${ruby}
  else
    chmod 644 ${ruby}
  fi
done

# fix empty documentation files
echo "%%%" >> texmf-dist/doc/latex/mathpazo/mapppl.tex
echo "%%%" >> texmf-dist/doc/latex/mathpazo/mapzplm.tex
for number in 1 2 3 5 7 8 10; do
  echo "%%%" >> texmf-dist/doc/latex/minitoc/add.mlt${number}
done
echo "%%%" >> texmf-dist/doc/latex/minitoc/add.mtc
for number in 1 2 3 5 7; do
  echo "%%%" >> texmf-dist/doc/latex/minitoc/add.mtc${number}
done
for number in 1 2 3 5 7 8; do
  echo "%%%" >> texmf-dist/doc/latex/minitoc/add.mlf${number}
done
for extension in mlf1 mlf6 mlt1 mlt3 mlt4 mlt5 mlt6 mtc plt2 plt3; do
  echo "%%%" >> texmf-dist/doc/latex/minitoc/minitoc-ex.${extension}
done
for extension in mtc mtc1 plt1 plt2 plt3 slf1 slf3 slf6 slt1 slt2 slt3 slt4 slt5 slt6; do
  echo "%%%" >> texmf-dist/doc/latex/minitoc/mini-art.${extension}
done

# fix empty version file
PST_CIRC_V="`basename texmf-dist/doc/generic/pst-circ/Version-* |cut -d"-" -f2`"
echo "Version ${PST_CIRC_V}" >> texmf-dist/doc/generic/pst-circ/Version-${PST_CIRC_V}

# turn off shell bang on these
#%%{__sed} -i '0,/^#!/s//##/' ${script}

%{__sed} -i '0,/^#!/s//##/' texmf-dist/tex/plain/cyrplain/makefmts.sh
%{__sed} -i '0,/^#!/s//##/' texmf-dist/tex/fontinst/cyrfinst/etc/showenc

# these should be in scripts with symlink to current location
mkdir -p texmf/scripts/hyphen/sh
pushd texmf/tex/generic/hyphen/
install -m755 bahyph.sh ../../../scripts/hyphen/sh/
rm bahyph.sh
ln -s ../../../scripts/hyphen/sh/bahyph.sh .
popd

# there should be no executable documentation files, and no shell bangs
for toplevel in texmf texmf-dist; do
  for file in `find ${toplevel}/doc -type f`; do
    chmod 644 ${file}
    if [ `head -1 ${file} |grep -c "^#!"` -eq 1 ]; then
      %{__sed} -i '0,/^#!/s//##/' ${file}
    fi
  done
done

%{_bindir}/find . -name '*.sh' -o -name '*.bat' | %{_bindir}/xargs %{__chmod} 0755
%{_bindir}/find ./texmf-dist/scripts/context/stubs/unix/* -type f | %{_bindir}/xargs %{__chmod} 0755

# these files owned by binary texlive-fonts package
rm texmf/web2c/{mktex.opt,mktexdir,mktexdir.opt,mktexnam,mktexnam.opt,mktexupd}
# these files owned by binary texlive-dvips package
rm -r texmf/dvips/base

%build

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}

install -d -m755 %{buildroot}%{_infodir}
install -p -m644 {eplain,tds}.info %{buildroot}%{_infodir}/

# install the texmf
%{__mkdir_p} %{buildroot}%{_texmf_main}
%{__mkdir_p} %{buildroot}%{_texmf_var}
%{__mkdir_p} %{buildroot}%{_texmf_conf}
%{__mkdir_p} %{buildroot}%{_texmf_vendor}

%{__cp} -a %{SOURCE2} %{buildroot}%{_texmf_main}/default.ls-R
%{__cp} -a %{SOURCE3} %{buildroot}%{_texmf_var}/default.ls-R
%{__cp} -a %{SOURCE4} %{buildroot}%{_texmf_conf}/default.ls-R
%{__cp} -a %{SOURCE5} %{buildroot}%{_texmf_vendor}/default.ls-R

%{__cp} -a texmf/* %{buildroot}%{_texmf_main}
%{__cp} -a texmf-var/* %{buildroot}%{_texmf_var}
%{__cp} -a texmf-dist/* %{buildroot}%{_texmf_vendor}

install -d -m755 %{buildroot}%{_texmf_main}/fonts/{cmap,sfd,type3,type42}

# move the configuration files and symlink them
install -d -m755 %{buildroot}%{_texmf_conf}/web2c
mv %{buildroot}%{_texmf_main}/web2c/*.cnf %{buildroot}%{_texmf_conf}/web2c/
for file in `find %{buildroot}%{_texmf_conf}/web2c/ -name '*.cnf'`; do
  filename="`basename ${file}`"
  ln -sf %{_texmf_conf}/web2c/${filename} %{buildroot}%{_texmf_main}/web2c/
done

touch %{buildroot}%{_texmf_main}/ls-R
touch %{buildroot}%{_texmf_var}/ls-R
install -d -m755 %{buildroot}%{_texmf_vendor}/{doc,tex}/{generic,latex}
install -d -m755 %{buildroot}%{_texmf_vendor}/fonts
touch %{buildroot}%{_texmf_vendor}/ls-R
touch %{buildroot}%{_texmf_conf}/ls-R

%{__mkdir_p} %{buildroot}%{_texmf_local}
touch %{buildroot}%{_texmf_local}/ls-R

install -d -m755 %{buildroot}%{_texmf_var}/xdvi
touch %{buildroot}%{_texmf_var}/xdvi/XDvi

# create macro file for building texlive
mkdir -p %{buildroot}%{_sysconfdir}/rpm/macros.d
cat <<EOF > %{buildroot}%{_sysconfdir}/rpm/macros.d/texlive.macros
%%_texmf_main     %%{_datadir}/texmf
%%_texmf_vendor   %%{_datadir}/texmf-texlive
%%_texmf_var      %%{_var}/lib/texmf
%%_texmf_conf     %%{_sysconfdir}/texmf
%%_texmf_local    %%{_usr}/local/share/texmf
EOF

%{__mkdir_p} %{buildroot}%{_texmf_conf}/tex/latex/config

pushd %{buildroot}%{_texmf_main}/tex/latex/config
    for i in *.cfg; do
        %{__mv} $i %{buildroot}%{_texmf_conf}/tex/latex/config/$i
        %{__ln_s} %{_texmf_conf}/tex/latex/config/$i .
    done
popd

%{__mkdir_p} %{buildroot}%{_texmf_conf}/tex/latex/pict2e

pushd %{buildroot}%{_texmf_vendor}/tex/latex/pict2e
    for i in *.cfg; do
        %{__mv} $i %{buildroot}%{_texmf_conf}/tex/latex/pict2e/$i
        %{__ln_s} %{_texmf_conf}/tex/latex/pict2e/$i .
    done
popd

%clean
rm -rf %{buildroot}

%post
[ -x %{_bindir}/texconfig-sys ] && LC_ALL=C %{_bindir}/texconfig-sys rehash 2> /dev/null || :
%_install_info tds.info
%_install_info eplain.info

#%%post common
# does not own any files, only directories - no texhash

%post context
[ -x %{_bindir}/texconfig-sys ] && LC_ALL=C %{_bindir}/texconfig-sys rehash 2> /dev/null || :

%post afm
[ -x %{_bindir}/texconfig-sys ] && LC_ALL=C %{_bindir}/texconfig-sys rehash 2> /dev/null || :

%post dvipdfm
[ -x %{_bindir}/texconfig-sys ] && LC_ALL=C %{_bindir}/texconfig-sys rehash 2> /dev/null || :

%post dvips
[ -x %{_bindir}/texconfig-sys ] && LC_ALL=C %{_bindir}/texconfig-sys rehash 2> /dev/null || :

%post fonts
# done in fonts because fonts package owns texhash
#  this is really only needed for build system
if [ ! -x %{_bindir}/texconfig-sys ]; then
  if [ -r %{_texmf_main}/default.ls-R ]; then
    %{__cp} -af %{_texmf_main}/default.ls-R %{_texmf_main}/ls-R || :
  fi
  if [ -r %{_texmf_main}/default.ls-R ]; then
    %{__cp} -af %{_texmf_var}/default.ls-R %{_texmf_var}/ls-R  || :
  fi
  if [ -r %{_texmf_conf}/default.ls-R ]; then
    %{__cp} -af %{_texmf_conf}/default.ls-R %{_texmf_conf}/ls-R  || :
  fi
  if [ -r %{_texmf_vendor}/default.ls-R ]; then
    %{__cp} -af %{_texmf_vendor}/default.ls-R %{_texmf_vendor}/ls-R  || :
  fi
else
  LC_ALL=C %{_bindir}/texconfig-sys rehash 2> /dev/null || :
fi

%post doc
[ -x %{_bindir}/texconfig-sys ] && LC_ALL=C %{_bindir}/texconfig-sys rehash 2> /dev/null || :

%post jadetex
[ -x %{_bindir}/texconfig-sys ] && LC_ALL=C %{_bindir}/texconfig-sys rehash 2> /dev/null || :

%post xmltex
[ -x %{_bindir}/texconfig-sys ] && LC_ALL=C %{_bindir}/texconfig-sys rehash 2> /dev/null || :

%preun
%_remove_install_info tds.info
%_remove_install_info eplain.info

%postun
[ -x %{_bindir}/texconfig-sys ] && LC_ALL=C %{_bindir}/texconfig-sys rehash 2> /dev/null || :

#%%postun common
#%[ -x %{_bindir}/texconfig-sys ] && LC_ALL=C %{_bindir}/texconfig-sys rehash 2> /dev/null || :

%postun context
[ -x %{_bindir}/texconfig-sys ] && LC_ALL=C %{_bindir}/texconfig-sys rehash 2> /dev/null || :

%postun afm
[ -x %{_bindir}/texconfig-sys ] && LC_ALL=C %{_bindir}/texconfig-sys rehash 2> /dev/null || :

%postun dvipdfm
[ -x %{_bindir}/texconfig-sys ] && LC_ALL=C %{_bindir}/texconfig-sys rehash 2> /dev/null || :

%postun dvips
[ -x %{_bindir}/texconfig-sys ] && LC_ALL=C %{_bindir}/texconfig-sys rehash 2> /dev/null || :

%postun fonts
[ -x %{_bindir}/texconfig-sys ] && LC_ALL=C %{_bindir}/texconfig-sys rehash 2> /dev/null || :

%postun doc
[ -x %{_bindir}/texconfig-sys ] && LC_ALL=C %{_bindir}/texconfig-sys rehash 2> /dev/null || :

%postun jadetex
[ -x %{_bindir}/texconfig-sys ] && LC_ALL=C %{_bindir}/texconfig-sys rehash 2> /dev/null || :

%postun xmltex
[ -x %{_bindir}/texconfig-sys ] && LC_ALL=C %{_bindir}/texconfig-sys rehash 2> /dev/null || :

%files
%defattr(-,root,root,0755)
%exclude %{_texmf_vendor}/tex4ht/
%{_texmf_main}/README
%{_texmf_vendor}/README
%config(noreplace) %{_sysconfdir}/rpm/macros.d/texlive.macros
%{_texmf_vendor}/bibtex/
%{_texmf_main}/bibtex/
%exclude %{_texmf_vendor}/bibtex/bst/context/
%dir %{_texmf_main}/fmtutil/
%{_texmf_vendor}/fonts/map/fontname/
%{_texmf_vendor}/makeindex/
%{_texmf_vendor}/metafont/
%{_texmf_vendor}/metapost/
%{_texmf_vendor}/mft/
%{_texmf_vendor}/omega/
%{_texmf_main}/scripts/
%{_texmf_vendor}/scripts/
%dir %{_texmf_main}/tex
%{_texmf_vendor}/tex/amstex/
##%{_texmf_vendor}/tex/context/
#%{_texmf_main}/tex/csplain/
%{_texmf_vendor}/tex/csplain/
%{_texmf_vendor}/tex/eplain/
%{_texmf_vendor}/tex/fontinst/
%{_texmf_main}/tex/fontinst/
%{_texmf_vendor}/tex/alatex/
%{_texmf_vendor}/tex/physe/
%{_texmf_vendor}/tex/phyzzx/
%{_texmf_vendor}/tex/psizzl/
%{_texmf_vendor}/tex/startex/
%{_texmf_vendor}/tex/texsis/
%exclude %{_texmf_vendor}/tex/xmltex/
%{_texmf_vendor}/tex/ytex/
%exclude %{_texmf_vendor}/tex/jadetex/
%exclude %{_texmf_vendor}/tex/latex3/
%dir %{_texmf_vendor}/tex/lambda
%{_texmf_vendor}/tex/lambda/antomega/
%{_texmf_vendor}/tex/lambda/config/
%{_texmf_vendor}/tex/lambda/oinuit/
%dir %{_texmf_vendor}/tex/lambda/base
%{_texmf_vendor}/tex/lambda/base/*.tex
%{_texmf_vendor}/tex/lambda/base/*.bgd
%{_texmf_vendor}/tex/lambda/base/*.lay
%{_texmf_vendor}/tex/lambda/base/*.hpn
%{_texmf_vendor}/tex/lambda/base/*.fd
%{_texmf_vendor}/tex/lambda/base/*.def
%{_texmf_vendor}/tex/lambda/base/*.sty
%{_texmf_vendor}/tex/mex/
%{_texmf_vendor}/tex/mltex/
%{_texmf_vendor}/tex/plain/
%{_texmf_vendor}/tex/texinfo/
# will result in a couple files being owned by texmf and texmf-fonts
#  texmf/tex/generic/babel/{frenchb.cfg,hyphen.cfg}
#  Not really worth worrying about.
%{_texmf_main}/tex/generic/
%{_texmf_vendor}/tex/generic/
%exclude %{_texmf_vendor}/tex/generic/context/
#
%{_texmf_main}/texdoctk/
%dir %{_texmf_main}/web2c
%{_texmf_main}/web2c/*.tcx
%{_texmf_main}/web2c/*.cnf
%exclude %{_texmf_main}/web2c/*.pool
# var
%{_texmf_var}/xdvi/XDvi
%{_texmf_var}/tex/
%dir %{_texmf_var}/fonts
%dir %{_texmf_var}/fonts/map
%dir %{_texmf_var}/fonts/map/dvips/updmap
%ghost %{_texmf_var}/fonts/map/dvips/updmap/*
%dir %{_texmf_var}/fonts/map/pdftex/updmap
%ghost %{_texmf_var}/fonts/map/pdftex/updmap/*
# info
%{_infodir}/tds.info*
%{_infodir}/eplain.info*
#
%{_texmf_main}/texconfig/g/
%{_texmf_main}/texconfig/v/
%{_texmf_main}/texconfig/x/
%exclude %{_texmf_main}/texconfig/g/generic
%exclude %{_texmf_main}/texconfig/generic
%exclude %{_texmf_main}/texconfig/README
%exclude %{_texmf_main}/texconfig/tcfmgr
%exclude %{_texmf_main}/texconfig/tcfmgr.map
%exclude %{_texmf_main}/texconfig/v/vt100
%exclude %{_texmf_main}/texconfig/x/xterm
#
%{_texmf_main}/chktex/.chktexrc
%{_texmf_main}/hbf2gf/
%{_texmf_vendor}/vtex/config/
%{_texmf_main}/ttf2pk/ttf2pk.cfg
%{_texmf_main}/ttf2pk/VPS.rpl
#
%{_texmf_main}/default.ls-R
%{_texmf_var}/default.ls-R
%{_texmf_conf}/default.ls-R
%{_texmf_vendor}/default.ls-R

# the common package should not own any installed files.
%files common
%defattr(-,root,root,0755)
%dir %{_texmf_main}
# for addon packages that want to put stuff in these directories
%dir %{_texmf_vendor}
%dir %{_texmf_vendor}/doc
%dir %{_texmf_main}/doc
%dir %{_texmf_vendor}/doc/generic
%dir %{_texmf_vendor}/doc/latex
# a few TDS directories (more need to be added)
%dir %{_texmf_vendor}/tex
%dir %{_texmf_vendor}/tex/generic
%dir %{_texmf_vendor}/tex/latex
%dir %{_texmf_vendor}/fonts
%dir %{_texmf_var}
%dir %{_texmf_var}/xdvi
%ghost %{_texmf_var}/xdvi/XDvi
# conf
%dir %{_texmf_conf}
%dir %{_texmf_conf}/web2c
%dir %{_texmf_conf}/tex
%dir %{_texmf_conf}/tex/latex
%dir %{_texmf_conf}/tex/latex/config
%dir %{_texmf_conf}/tex/latex/pict2e
%config(noreplace) %{_texmf_conf}/tex/latex/config/*.cfg
%config(noreplace) %{_texmf_conf}/tex/latex/pict2e/*.cfg

%files context
%defattr(-,root,root,0755)
%{_texmf_vendor}/bibtex/bst/context/
%{_texmf_vendor}/context/
%{_texmf_vendor}/fonts/afm/hoekwater/context/
%{_texmf_vendor}/fonts/enc/dvips/context/
#%{_texmf_vendor}/fonts/map/dvipdfm/context/
#%{_texmf_vendor}/fonts/map/pdftex/context/
%{_texmf_vendor}/fonts/pfm/hoekwater/context/
%{_texmf_vendor}/fonts/tfm/hoekwater/context/
%{_texmf_vendor}/fonts/type1/hoekwater/context/
%{_texmf_vendor}/metapost/context/
%{_texmf_vendor}/scripts/context/
%{_texmf_vendor}/tex/context/
%{_texmf_vendor}/tex/generic/context/
%{_texmf_vendor}/tex/latex/context/

%files cmsuper
%defattr(-,root,root,0755)
%{_texmf_vendor}/fonts/afm/public/cm-super/
%{_texmf_vendor}/fonts/type1/public/cm-super/
%{_texmf_vendor}/fonts/enc/dvips/cm-super/
#%{_texmf_vendor}/fonts/map/dvips/cm-super/

%files afm
%defattr(0644,root,root,0755)
%{_texmf_vendor}/fonts/afm/
%exclude %{_texmf_vendor}/fonts/afm/hoekwater/context/
%exclude %{_texmf_vendor}/fonts/afm/public/cm-super/

%files dvipdfm
%defattr(-,root,root,0755)
%{_texmf_main}/dvipdfm/
%exclude %{_texmf_main}/dvipdfm/EUC-UCS2
%exclude %{_texmf_main}/dvipdfm/UniKSCms-UCS2-H
%exclude %{_texmf_main}/dvipdfm/UniKSCms-UCS2-V
%dir %{_texmf_var}/fonts/map/dvipdfm
%dir %{_texmf_var}/fonts/map/dvipdfm/updmap
%ghost %{_texmf_var}/fonts/map/dvipdfm/updmap/*
%{_texmf_main}/fonts/map/dvipdfm/
%{_texmf_vendor}/fonts/map/dvipdfm/
%{_texmf_var}/dvipdfm/

%files dvips
%defattr(-,root,root,0755)
%{_texmf_main}/dvips/
%exclude %{_texmf_main}/dvips/gsftopk/render.ps
%{_texmf_var}/dvips/
%{_texmf_vendor}/dvips/
# these are what are also needed by fonts
%dir %{_texmf_main}/fonts/enc
%dir %{_texmf_main}/fonts/map
%dir %{_texmf_main}/fonts
%{_texmf_main}/fonts/enc/dvips/
%{_texmf_vendor}/fonts/enc/dvips/
%exclude %{_texmf_vendor}/fonts/enc/dvips/context/
%exclude %{_texmf_vendor}/fonts/enc/dvips/cm-super/
%{_texmf_main}/fonts/map/dvips/
%{_texmf_vendor}/fonts/map/dvips/
# not 100% positive this is right place
%{_texmf_vendor}/fonts/enc/pdftex/
%{_texmf_main}/fonts/map/pdftex/
%{_texmf_vendor}/fonts/map/pdftex/

%files fonts
%defattr(-,root,root,0755)
%ghost %{_texmf_main}/ls-R
%ghost %{_texmf_vendor}/ls-R
%ghost %{_texmf_conf}/ls-R
%ghost %{_texmf_var}/ls-R
%config(noreplace) %{_texmf_conf}/web2c/*.cnf
%{_texmf_main}/web2c/*.cnf
#%{_texmf_main}/default.ls-R
%dir %{_texmf_main}/fonts/cmap
%{_texmf_vendor}/fonts/ofm/
%{_texmf_vendor}/fonts/opentype/
%{_texmf_vendor}/fonts/ovf/
%{_texmf_vendor}/fonts/ovp/
%{_texmf_vendor}/fonts/pfm/
%exclude %{_texmf_vendor}/fonts/pfm/hoekwater/context/
%dir %{_texmf_vendor}/fonts/pk
%dir %{_texmf_main}/fonts/sfd
%{_texmf_main}/fonts/enc/
%{_texmf_main}/fonts/lig/
%{_texmf_main}/fonts/map/
%exclude %{_texmf_main}/fonts/map/dvipdfm/
%exclude %{_texmf_main}/fonts/map/dvips/
%exclude %{_texmf_main}/fonts/map/pdftex/
%{_texmf_main}/fonts/sfd/*
#%{_texmf_main}/fonts/source/
%{_texmf_vendor}/fonts/source/
#%{_texmf_main}/fonts/tfm/
%{_texmf_vendor}/fonts/tfm/
%exclude %{_texmf_vendor}/fonts/tfm/hoekwater/context/
#%{_texmf_main}/fonts/type1/
%{_texmf_vendor}/fonts/type1/
%exclude %{_texmf_vendor}/fonts/type1/public/cm-super/
%{_texmf_vendor}/fonts/truetype/
%dir %{_texmf_main}/fonts/type3
%dir %{_texmf_main}/fonts/type42
#%{_texmf_main}/fonts/vf/
%{_texmf_vendor}/fonts/vf/
#%{_texmf_main}/fonts/vf-cnv/
#
%{_texmf_vendor}/tex/plain/cyrplain/cyrtex.cfg
%{_texmf_vendor}/tex/generic/babel/frenchb.cfg
%{_texmf_vendor}/tex/generic/babel/hyphen.cfg
#%{_texmf_main}/tex/generic/config/fontmath.cfg
#%{_texmf_main}/tex/generic/config/fonttext.cfg
#%{_texmf_main}/tex/generic/config/preload.cfg
%{_texmf_vendor}/tex/lambda/base/omarab.cfg
%{_texmf_vendor}/tex/lambda/base/omlgc.cfg
# check with bin package
%{_texmf_main}/web2c/updmap.cfg
# texmf-var
#%{_texmf_var}/default.ls-R
%{_texmf_var}/xdvi/XDvi
%exclude %{_texmf_main}/xdvi/XDvi
%exclude %{_texmf_main}/xdvi/xdvi.cfg
%{_texmf_var}/web2c/mktex.cnf
%{_texmf_main}/xdvi/pixmaps
%exclude %{_texmf_main}/xdvi/pixmaps/toolbar.xpm
%exclude %{_texmf_main}/xdvi/pixmaps/toolbar2.xpm
#
%{_texmf_vendor}/fonts/map/
%{_texmf_vendor}/fonts/misc/

%files latex
%defattr(-,root,root,0755)
#%{_texmf_main}/tex/cslatex/
%{_texmf_vendor}/tex/cslatex/
%{_texmf_main}/tex/latex/
%{_texmf_vendor}/tex/latex/
%{_texmf_vendor}/tex/platex/
%{_texmf_vendor}/tex/xelatex/
##%{_texmf_vendor}/context/data/latex-scite.properties

%files doc
%defattr(0644,root,root,0755)
%doc %{_texmf_main}/doc/
%doc %{_texmf_vendor}/doc/
%exclude %{_texmf_main}/doc/bibtex8/00readme.txt
%exclude %{_texmf_main}/doc/bibtex8/HISTORY
%exclude %{_texmf_main}/doc/bibtex8/csfile.txt
%exclude %{_texmf_main}/doc/bibtex8/file_id.diz

%files usrlocal
%defattr(-,root,root,0755)
%dir %{_texmf_local}
%ghost %{_texmf_local}/ls-R

%files jadetex
%defattr(-,root,root,0755)
%{_texmf_vendor}/tex/jadetex/

%files xmltex
%defattr(-,root,root,0755)
%{_texmf_vendor}/tex/xmltex/

