# revision 25552
# category Package
# catalog-ctan /macros/latex/contrib/lmake
# catalog-date 2012-03-02 00:29:05 +0100
# catalog-license lppl1.2
# catalog-version 1.0
Name:		texlive-lmake
Version:	1.0
Release:	7
Summary:	Process lists to do repetitive actions
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/lmake
License:	LPPL1.2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lmake.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lmake.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lmake.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides commands to simplify processing of
sequential list-like structures, such as making a series of
'similar' commands from a list of names.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/lmake/lmake.sty
%doc %{_texmfdistdir}/doc/latex/lmake/README
%doc %{_texmfdistdir}/doc/latex/lmake/lmake.pdf
#- source
%doc %{_texmfdistdir}/source/latex/lmake/lmake.dtx
%doc %{_texmfdistdir}/source/latex/lmake/lmake.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Fri Mar 09 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.0-2
+ Revision: 783481
- rebuild without scriptlet dependencies

* Wed Mar 07 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0-1
+ Revision: 783047
- Import texlive-lmake
- Import texlive-lmake

