Name:		texlive-lmake
Version:	25552
Release:	1
Summary:	Process lists to do repetitive actions
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/lmake
License:	LPPL1.2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lmake.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lmake.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lmake.source.r%{version}.tar.xz
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
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
