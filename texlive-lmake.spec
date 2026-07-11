%global tl_name lmake
%global tl_revision 25552

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Process lists to do repetitive actions
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/lmake
License:	lppl1.2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lmake.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lmake.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lmake.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides commands to simplify processing of sequential list-
like structures, such as making a series of 'similar' commands from a
list of names.

